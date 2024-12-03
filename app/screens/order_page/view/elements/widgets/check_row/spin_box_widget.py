from PySide6.QtWidgets import QLabel, QWidget
from PySide6.QtCore import Qt

from app.screens.order_page.view.elements.widgets.check_row.modals.edit_quantity_modal import EditQuantityDialog
from app.utils.constants import Colors

class CustomSpinBox(QWidget):
    def __init__(self, basket_product, update_callback, parent=None):
        super().__init__(parent)
        self.basket_product = basket_product
        self.update_callback = update_callback

        self.setFixedSize(80, 40)

        self.label = QLabel(self)
        self.set_text(self.basket_product.quantity)

        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet(f"""
                            QWidget
                            {{
                                margin-left: 0;
                                background-color: white;
                                font-size: 24px;
                                color: black;
                                border-top: 1px solid {Colors.SOFT_BLUE};
                                border-bottom: 1px solid {Colors.SOFT_BLUE};
                            }}
                            """)
        self.label.setFixedSize(80, 40)

    def mousePressEvent(self, event):
        try:
            dialog = EditQuantityDialog(self.basket_product, self.update_callback, self)
            if dialog.exec():
                self.label.setText(str(self.basket_product.quantity))
        except Exception as e:
            print(f"[Error] mousePressEvent in quantity view failed: {e}")
        super().mousePressEvent(event)

    def set_text(self, text):
        self.label.setText(self.textFromValue(str(text)))

    def get_text(self):
        return self.label.text()

    def textFromValue(self, value):
        try:
            float_value = float(value)
            if float_value.is_integer():
                return str(int(float_value))
            else:
                return str(float_value)
        except ValueError:
            return value