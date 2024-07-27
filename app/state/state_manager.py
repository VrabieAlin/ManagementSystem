import json
import os

from PySide6.QtCore import Signal, QObject

from app.utils.decorators.singletone import Singleton
from app.utils.decorators.state_decorators import save_after


@Singleton
class StateManager(QObject):
    state_changed = Signal()  # for reactivity of the app
    def __init__(self):
        super().__init__()
        self.file_path = "state.json"
        self.logged_in = False
        self.user_name = None
        self.order_page_state = {'current_category': 1}

        self.load_state()

    def load_state(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                data = json.load(file)
                self.logged_in = data.get("logged_in", False)
                self.user_name = data.get("user_name", None)
                self.order_page_state = data.get("order_page_state", {'current_category': 1})

    @save_after()
    def login(self, user_name):
        self.logged_in = True
        self.user_name = user_name

    @save_after()
    def logout(self):
        self.logged_in = False
        self.user_name = None

    @save_after()
    def change_category(self, new_category_id):
        self.order_page_state['current_category'] = new_category_id