import json
import os

from PySide6.QtCore import Signal, QObject
from box import Box


class BaseState(QObject):
    def __init__(self, moked_data):
        super().__init__()
        self.file_path = "state.json"
        self.moked_data = moked_data
        self.context = Box(moked_data)

        self.load_state()

    def load_state(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as file:
                data = json.load(file)
                for key, value in self.moked_data.items():
                    self.context[key] = data.get(key, value)