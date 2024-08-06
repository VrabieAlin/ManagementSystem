import json
import os

from PySide6.QtCore import Signal, QObject

from app.utils.decorators.singletone import Singleton
from app.utils.decorators.state_decorators import save_after
from app.state.base_state import BaseState
from box import Box

moked_data = {
        "logged_in": False,
        "user_name": None
}


@Singleton
class UserState(BaseState):
    state_changed = Signal()  # for reactivity of the app
    def __init__(self):
        super().__init__(moked_data)

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


