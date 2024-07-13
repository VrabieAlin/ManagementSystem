from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout

from app.utils.widgets.widgets_utils import WidgetUtils


class MenuModal(QDialog):
    menu_button = Signal(str)

    def __init__(self, text_buttons):
        super().__init__()

        # Remove the app bar present in os applications (the one that have a title and minimize, maximize, close button)
        self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.FramelessWindowHint)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)

        # Create a menu modal with buttons. As we don't know now what button we have, we'll choose a modal with 3
        # buttons per row
        buttons = []
        cnt = 0
        layout_modal = QVBoxLayout()
        for i in range(len(text_buttons)):
            btn = WidgetUtils.createHExpandableButton(text_buttons[i])
            btn.clicked.connect(lambda checked, text=text_buttons[i]: self.on_clicked(text))
            buttons.append(btn)
            cnt += 1
            # End of a row
            if cnt == 3:
                row_layout = QHBoxLayout()
                for widget in buttons:
                    row_layout.addWidget(widget)
                layout_modal.addLayout(row_layout)
                buttons.clear()
                cnt = 0

        self.setLayout(layout_modal)

    def on_clicked(self, btn_text):
        self.menu_button.emit(btn_text)
        self.close()
