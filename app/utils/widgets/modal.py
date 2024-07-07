from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QHBoxLayout

from app.utils.widgets.widgets_utils import WidgetUtils


class Modal(QDialog):
    accepted = Signal()
    rejected = Signal()

    def __init__(self, text, accept_btn_text, reject_btn_text):
        super().__init__()

        # Remove the app bar present in os applications (the one that have a title and minimize, maximize, close button)
        self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.FramelessWindowHint)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)

        # Create a horizontal layout to put the 2 buttons for accept and reject modal
        buttons_layout = QHBoxLayout()
        buttons_layout.setContentsMargins(0, 0, 0, 0)
        buttons_layout.setSpacing(100)

        # The accept button
        accept_btn = WidgetUtils.createHExpandableButton(accept_btn_text)
        buttons_layout.addStretch()
        buttons_layout.addWidget(accept_btn)

        # The reject button
        close_button = WidgetUtils.createHExpandableButton(reject_btn_text)
        buttons_layout.addStretch()
        buttons_layout.addWidget(close_button)

        # Set callbacks for accept/reject modal
        accept_btn.clicked.connect(self.on_ok_clicked)
        close_button.clicked.connect(self.on_cancel_clicked)

        # Assemble the elements into a modal
        layout = QVBoxLayout()
        message = QLabel(text)
        layout.addWidget(message)
        layout.addLayout(buttons_layout)
        self.setLayout(layout)

    def on_ok_clicked(self):
        self.accepted.emit()
        self.close()

    def on_cancel_clicked(self):
        self.rejected.emit()
        self.close()
