from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt
from app.utils.constants import Colors

class PrimaryButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setFixedSize(250, 100)
        self.set_style()

    def set_style(self):
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {Colors.SOFT_BLUE};
                color: {Colors.WHITE};
                border: 1px solid {Colors.SOFT_BLUE};
                border-radius: 4px;
                padding: 10px 20px;
                font-size: 20px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {Colors.DARKER_BLUE};
            }}
            QPushButton:pressed {{
                background-color: {Colors.EVEN_DARKER_BLUE};
            }}
        """)
