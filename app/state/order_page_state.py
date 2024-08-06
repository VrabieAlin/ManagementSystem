import json
import os

from PySide6.QtCore import Signal, QObject

from app.utils.decorators.singletone import Singleton
from app.utils.decorators.state_decorators import save_after
from app.state.base_state import BaseState
from box import Box

moked_data = {
    "order_page_state": {
        "table_id": 1,
        "current_category": 1
    },
    "tables_orders": {}
}


@Singleton
class OrderPageState(BaseState):
    state_changed = Signal()  # for reactivity of the app
    category_change = Signal()
    product_added = Signal(int, dict)

    def __init__(self):
        super().__init__(moked_data)

    @save_after()
    def change_category(self, new_category_id):
        self.context.order_page_state.current_category = new_category_id
        self.category_change.emit()
        return self.context

    @save_after()
    def update_check(self, params):
        table_id, product = params

        #TO DO: add product in state

        self.product_added.emit(table_id, product)
        return self.context

    @save_after()
    def select_new_table(self, new_table_id):
        self.context.order_page_state.table_id = new_table_id
        self.context.order_page_state.current_category = 1

        return self.context
