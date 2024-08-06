from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QSizePolicy, QGridLayout
from app.screens.order_page.view.elements.widgets.spin_widget import SpinWidget
from PySide6.QtCore import Qt
from app.screens.order_page.view.elements.widgets.test import Test

class ProductWidget(QWidget):
    def __init__(self, product, quantity, update_callback):
        super().__init__()
        self.product = product
        self.update_callback = update_callback
        self.quantity = quantity
        self.setContentsMargins(0, 0, 0, 0)

        self.load_view()

    def load_view(self):
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.setMinimumHeight(50)

        self.setLayout(self.layout)

        self.setup_name_label()
        self.setup_spin_widget()
        self.setup_price_label()

    def setup_name_label(self):
        self.name_label = QLabel(self.product["name"])
        self.name_label.setStyleSheet("font-size: 24px; color: #000000; padding: 0 5px;")
        self.layout.addWidget(self.name_label, 1)

    def setup_spin_widget(self):
        self.parent_spin = QWidget()
        self.parent_layout = QGridLayout(self.parent_spin)

        self.spin_widget = SpinWidget(self.quantity, self.update_quantity)
        self.spin_widget.setAutoFillBackground(True)
        self.spin_widget.setParent(self.parent_spin)

        self.parent_layout.addWidget(self.spin_widget, 1, 1)

        self.layout.addWidget(self.parent_spin, 1)

    def setup_price_label(self):
        self.price_label = QLabel(f"{self.product['price'] * self.quantity:.2f} RON")
        self.price_label.setStyleSheet("font-size: 24px; color: #000000; padding: 0 5px;")
        self.price_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.layout.addWidget(self.price_label, 1)

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
        self.price_label.setText(f"{self.product['price'] * self.quantity:.2f} RON")
        self.update_callback(self.product['id'], new_quantity)

    def refresh_spinner(self, new_spinner_value):
        self.spin_widget.set_value(new_spinner_value)