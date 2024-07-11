from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QDialog, QVBoxLayout

from app.utils.widgets.widgets_utils import WidgetUtils


class InputModal(QDialog):
    input_modal = Signal()

    def __init__(self, input_text, input_placeholder, input_type, btn_text):
        super().__init__()

        # Remove the app bar present in os applications (the one that have a title and minimize, maximize, close button)
        self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.FramelessWindowHint)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)

        layout = QVBoxLayout()
        input_el = WidgetUtils.createHExpandableInput(input_text, input_placeholder, input_type)
        btn = WidgetUtils.createHExpandableButton(btn_text)
        btn.clicked.connect(self.on_clicked)
        layout.addLayout(input_el)
        layout.addWidget(btn)

        self.setLayout(layout)

    def on_clicked(self):
        self.input_modal.emit()
        self.close()
