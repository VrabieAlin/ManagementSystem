import json
import os

from PySide6.QtCore import QObject, Signal
from box import Box

from app.utils.decorators.singletone import Singleton
from app.utils.decorators.state_decorators import save_after


@Singleton
class LocationEditorDragState(QObject):
    state_changed = Signal()  # for reactivity of the app
    dragged_item_signal = Signal()

    def __init__(self):
        super().__init__()
        self.file_path = "state.json"

        self.context = Box(
            {
                "dragged_item":
                 {
                     'id': None,
                     'image': None
                 },
            })

        self.load_state()

    def load_state(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                data = json.load(file)
                self.context.dragged_item = data.get("dragged_item",{
                    'image': None,
                    'id': None
                 })

    @save_after()
    def save_dragged_object_info(self, object):
        self.context.dragged_item.image = object.image
        self.context.dragged_item.id = object.id
        self.dragged_item_signal.emit()
        return self.context