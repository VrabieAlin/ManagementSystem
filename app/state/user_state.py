import json
import os

from PySide6.QtCore import Signal, QObject

from app.utils.decorators.singletone import Singleton
from app.utils.decorators.state_decorators import save_after
from box import Box


@Singleton
class UserState(QObject):
    state_changed = Signal()  # for reactivity of the app
    def __init__(self):
        super().__init__()
        self.file_path = "state.json"

        self.context = Box({"logged_in": False,
                            "user_name": None})

        self.load_state()

    def load_state(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                data = json.load(file)
                self.context.logged_in = data.get("logged_in", False)
                self.context.user_name = data.get("user_name", None)

    @save_after()
    def login(self, user_name):
        self.context.logged_in = True
        self.context.user_name = user_name
        return self.context

    @save_after()
    def logout(self):
        self.context.logged_in = False
        self.context.user_name = None
        return self.context


