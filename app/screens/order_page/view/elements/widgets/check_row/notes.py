from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QVBoxLayout, QTextEdit
from PySide6.QtGui import QFont

from app.screens.order_page.model.basket_product import BasketProduct
from app.utils.constants import Colors


class NotesEditor(QDialog):
    def __init__(self, basket_product: BasketProduct, close_callback, parent=None):
        super().__init__(parent)
        self.setContentsMargins(0, 0, 0, 0)
        self.close_callback = close_callback
        self.basket_product = basket_product

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Dialog)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)

        self.load_view()

    def load_view(self):
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(5, 5, 5, 0)
        self.setStyleSheet(f"""
                                background-color: {Colors.SOFT_BLUE_2};
                                color: {Colors.SOFT_BLUE};
                                border: 1 solid {Colors.SOFT_BLUE};
                                border-radius: 5px;
                                font-size: 20px;
                              """)

        self.text_edit = QTextEdit(self)
        self.text_edit.setText(self.basket_product.notes)

        # Set font for QTextEdit
        font = QFont("Arial", 16)
        self.text_edit.setFont(font)

        self.layout.addWidget(self.text_edit)
        self.setLayout(self.layout)

        self.setFixedSize(self.parent().width() - 10, 120)

    def closeEvent(self, event):
        print("Close notes editor")
        if self.close_callback:
            self.close_callback()
        super().closeEvent(event)