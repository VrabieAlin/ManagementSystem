import json
import os

from PySide6.QtCore import Signal, QObject

from app.utils.decorators.singletone import Singleton
from app.state.order_page_state import OrderPageState
from app.state.user_state import UserState
from app.utils.decorators.state_decorators import save_after


@Singleton
class StateManager(QObject):
    state_changed = Signal()  # for reactivity of the app
    def __init__(self):
        super().__init__()
        self.file_path = "state.json" #key: table_id, value: [{product_id, total_price, item_price, quantity, state: ORDERED/IN_KITCHEN/EDITOR, name, waiter_id}]

        self.load_state()


    def load_state(self):
        pass

    def reset_state(self): #In caz de update in state trebuie start fisierul de save state si refacut cu noul format
        pass

    @save_after()
    def login(self, user_name):
        self.logged_in = True
        self.user_name = user_name

    @save_after()
    def logout(self):
        self.logged_in = False
        self.user_name = None


