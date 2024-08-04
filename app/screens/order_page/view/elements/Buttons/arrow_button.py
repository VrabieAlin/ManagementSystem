from PySide6.QtWidgets import QPushButton

from app.utils.constants import Colors


class ArrowButton(QPushButton):
    def __init__(self, text, available=True, parent=None):
        super().__init__(text, parent)
        self.available = available
        self.setFixedSize(100, 100)
        self.set_style()

    def set_availability(self, available = True):
        self.available = available
        if self.available:
            self.show()
        else:
            self.hide()
        self.set_style()

    def set_style(self):
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {Colors.SOFT_BLUE if self.available else Colors.DARK_GRAY};
                color: {Colors.WHITE};
                border: 1px solid {Colors.SOFT_BLUE if self.available else Colors.DARK_GRAY};
                border-radius: 50%;
                padding: 10px 20px;
                font-size: 20px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {Colors.SOFT_BLUE if self.available else Colors.DARK_GRAY};
            }}
            QPushButton:pressed {{
                background-color: {Colors.SOFT_BLUE if self.available else Colors.DARK_GRAY};
            }}
        """)
