from PySide6.QtWidgets import QSpinBox, QDoubleSpinBox, QTextEdit
from PySide6.QtCore import Qt, QEvent

from app.screens.order_page.view.elements.widgets.check_row.modals.edit_quantity_modal import EditQuantityDialog
from app.utils.constants import Colors

class CustomSpinBox(QTextEdit):
    def __init__(self, basket_product, update_callback, parent=None):
        super().__init__(parent)
        self.basket_product = basket_product
        self.update_callback = update_callback

        self.setFixedSize(80, 40)
        self.setText(self.textFromValue(self.basket_product.quantity))
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet(f"""
                            QTextEdit
                            {{
                                margin-left: 0;
                                background-color: white;
                                font-size: 24px;
                                color: black;
                                border-top: 1px solid {Colors.SOFT_BLUE};
                                border-bottom: 1px solid {Colors.SOFT_BLUE};
                            }}
                            """)

    def mousePressEvent(self, event):
        dialog = EditQuantityDialog(self.basket_product, self.update_callback, self)
        if dialog.exec():
            self.setText(str(self.basket_product.quantity))
        super().mousePressEvent(event)

    def textFromValue(self, value):
        if value == int(value):
            return str(int(value))
        else:
            return str(value)
