from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QColor
from PySide6.QtCore import Qt
from app.utils.constants import Colors
class CustomLabel1(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setAlignment(Qt.AlignCenter)
        self.set_style()

    def set_style(self):
        self.setStyleSheet(f"""
            QLabel {{
                color: {Colors.DARK_GRAY};  /* Dark Gray */
                font-size: 20px;
                font-weight: normal;
            }}
        """)