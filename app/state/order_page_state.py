import json
import os

from PySide6.QtCore import Signal, QObject
from typing import Tuple

from app.utils.decorators.singletone import Singleton
from app.utils.decorators.state_decorators import save_after
from app.state.base_state import BaseState
from box import Box
from app.screens.order_page.model.product import Product
from app.screens.order_page.model.basket_product import BasketProduct

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
    reload_check_signal = Signal(BasketProduct)
    product_added_signal = Signal(int, Product)

    def __init__(self):
        super().__init__(moked_data)

    @save_after()
    def change_category(self, new_category_id):
        self.context.order_page_state.current_category = new_category_id
        self.category_change.emit()
        return self.context

    @save_after()
    def update_check(self, params: Tuple[str, BasketProduct]):
        table_id, basket_product = params

        #TO DO: add product in state
        if table_id not in self.context.tables_orders:
            self.context.tables_orders[table_id] = {}
        self.context.tables_orders[table_id][basket_product.basket_id] = basket_product.to_dict()


        self.reload_check_signal.emit(basket_product) #Used in check.py to refresh the check
        return self.context

    @save_after()
    def add_product_to_basket(self, params: Tuple[int, Product]):
        table_id, product = params

        self.product_added_signal.emit(table_id, copy.deepcopy(product))
        return self.context


    @save_after()
    def select_new_table(self, new_table_id):
        self.context.order_page_state.table_id = new_table_id
        self.context.order_page_state.current_category = 1

        return self.context
