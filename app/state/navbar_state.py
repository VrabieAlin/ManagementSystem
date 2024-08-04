import json
import os

from PySide6.QtCore import Signal, QObject
from box import Box

from app.utils.decorators.singletone import Singleton
from app.utils.decorators.state_decorators import save_after


@Singleton
class NavbarState(QObject):
    state_changed = Signal()  # for reactivity of the app
    view_selected = Signal()

    def __init__(self):
        super().__init__()
        self.file_path = "state.json"

        self.context = Box(
            {
                "active_view": 'teste',
            })

        self.load_state()

    def load_state(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                data = json.load(file)
                self.context.active_view = data.get("active_view", 'teste')

    @save_after()
    def change_view(self, view):
        self.context.active_view = view
        self.view_selected.emit()
        return self.context
