import json
import os
import random
import string
import traceback

from PySide6.QtCore import Signal, QObject
from typing import Tuple

from app.utils.decorators.singletone import Singleton
from app.utils.decorators.state_decorators import save_after
from app.state.base_state import BaseState
from box import Box
from app.screens.order_page.model.product import Product
from app.screens.order_page.model.basket_product import BasketProduct
from app.utils.constants import ORDERED_PRODUCT_STATUS as PRODUCT_STATUS

import copy

moked_data = {
    "order_page_state": {
        "table_id": 1,
        "current_category": 1
    },
    "tables_orders":  {} # key - table_id, value - {basket_id: BasketProduct}
}


@Singleton
class OrderPageState(BaseState):
    state_changed = Signal()  # for reactivity of the app
    category_change = Signal()
    reload_check_signal = Signal(str)
    product_added_signal = Signal(int, BasketProduct)

    def __init__(self):
        super().__init__(moked_data)

    @save_after()
    def change_category(self, new_category_id):
        self.context.order_page_state.current_category = new_category_id
        self.category_change.emit()
        return self.context

    @save_after()
    def update_check(self, params: Tuple[str, BasketProduct]):
        print("Updated product to basket")
        table_id, basket_product = params

        #TO DO: add product in state
        if table_id not in self.context.tables_orders:
            self.context.tables_orders[table_id] = {}
        self.context.tables_orders[table_id][basket_product.basket_id] = basket_product.to_dict()

        self.reload_check_signal.emit(table_id) #Used in check.py to refresh the check
        return self.context

    def generate_basket_id(self):
        lungime = 20
        caractere = string.ascii_letters + string.digits + string.punctuation
        sir_random = ''.join(random.choice(caractere) for _ in range(lungime))

        return sir_random

    def get_basket_id_from_product(self, table_id, product_id, product_status = PRODUCT_STATUS.NEW):
        try:
            for basket_id, basket_product in self.context.tables_orders[table_id].items():
                if basket_product.product.id == product_id and product_status == basket_product.status:
                    return basket_id
        except Exception as e:
            print(f"[Error check] Could not get basket id from product ({e})")
            print(f"[Error check] Stack trace: ({traceback.format_exc()})")
        return None

    def create_basket_product(self, table_id: int, product: Product) -> BasketProduct:
        table_id = str(table_id)
        if table_id not in self.context.tables_orders:
            self.context.tables_orders[table_id] = {}

        basket_id = self.get_basket_id_from_product(table_id, product.id)
        if basket_id is not None:
            self.context.tables_orders[table_id][basket_id]['quantity'] += 1
            return BasketProduct.from_dict(self.context.tables_orders[table_id][basket_id])

        basket_id = self.generate_basket_id()
        basket_product = BasketProduct(basket_id, 1, table_id, PRODUCT_STATUS.NEW, product)
        self.context.tables_orders[table_id][basket_id] = basket_product.to_dict()
        return basket_product

    @save_after()
    def add_product_to_basket(self, params: Tuple[int, Product]):
        print("Added product to basket")
        table_id, product = params
        basket_product = self.create_basket_product(table_id, product)
        self.product_added_signal.emit(table_id, copy.deepcopy(basket_product))
        return self.context

    @save_after()
    def void_element(self, params: Tuple[str, BasketProduct]):
        print("Deleted product from basket")
        try:
            table_id, basket_product = params
            del self.context.tables_orders[table_id][basket_product.basket_id]
            self.reload_check_signal.emit(table_id)
        except Exception as e:
            print(f"Could not delete the product from state: {e}")

        return self.context

    @save_after()
    def void_total_new(self, table_id):
        print("Deleted all products from basket")
        try:
            if table_id in self.context.tables_orders:
                products_to_remove = [basket_id for basket_id, product in self.context.tables_orders[table_id].items() if product['status'] == 'new']
                for basket_id in products_to_remove:
                    del self.context.tables_orders[table_id][basket_id]
                self.reload_check_signal.emit(table_id)
        except Exception as e:
            print(f"Could not delete new products from the table id {table_id} from state: {e}")
        return self.context

    @save_after()
    def select_new_table(self, new_table_id):
        self.context.order_page_state.table_id = new_table_id
        self.context.order_page_state.current_category = 1

        return self.context
