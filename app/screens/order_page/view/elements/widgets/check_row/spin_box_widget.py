from PySide6.QtWidgets import QSpinBox
from PySide6.QtCore import Qt

from app.screens.order_page.view.elements.widgets.check_row.modals.edit_quantity_modal import EditQuantityDialog
from app.utils.constants import Colors

class CustomSpinBox(QSpinBox):
    def __init__(self, basket_product, update_callback, parent=None):
        super().__init__(parent)
        self.basket_product = basket_product
        self.update_callback = update_callback
        self.setButtonSymbols(QSpinBox.ButtonSymbols.NoButtons)  # Hide the increment and decrement buttons
        self.setFixedSize(60, 40)
        self.setValue(self.basket_product.quantity)
        self.setMinimum(1)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.valueChanged.connect(self.update_quantity)
        self.setStyleSheet(f"""
                            QSpinBox
                            {{
                                margin-left: 0;
                                background-color: white;
                                font-size: 24px;
                                color: black;
                                border-top: 1px solid {Colors.SOFT_BLUE};
                                border-bottom: 1px solid {Colors.SOFT_BLUE};
                            }}
                            """)

    def update_quantity(self):
        self.update_callback(self.value())

    def mousePressEvent(self, event):
        dialog = EditQuantityDialog(self.basket_product, self.update_callback, self)
        if dialog.exec():
            print("Quantity updated:", self.basket_product.quantity)
        #super().mousePressEvent(event)