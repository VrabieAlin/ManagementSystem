import json
import os

from PySide6.QtCore import Signal, QObject

from app.utils.decorators.singletone import Singleton
from app.utils.decorators.state_decorators import save_after
from box import Box


@Singleton
class OrderPageState(QObject):
    state_changed = Signal()  # for reactivity of the app
    category_change = Signal()
    product_added = Signal(int, dict)

    def __init__(self):
        super().__init__()
        self.file_path = "state.json"

        self.context = Box({"order_page_state": {'table_id': 1,
                                                 'current_category': 1},
                            "tables_orders": {}})

        self.load_state()

    def load_state(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                data = json.load(file)
                self.context.order_page_state = data.get("order_page_state", {'table_id': 1, 'current_category': 1})
                self.context.tables_orders = data.get("tables_orders", {})

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
