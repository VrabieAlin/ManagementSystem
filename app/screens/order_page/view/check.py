#Layout cu nota: contine fiecare item comandat

from PySide6.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QWidget, QLabel, QSpinBox
)

from app.state.order_page_state import OrderPageState
from app.utils.constants import Colors


class ProductWidget(QWidget):
    def __init__(self, product, quantity, update_callback):
        super().__init__()
        self.product = product
        self.update_callback = update_callback

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.name_label = QLabel(product["name"])
        self.layout.addWidget(self.name_label)

        self.quantity_spinbox = QSpinBox()
        self.quantity_spinbox.setValue(quantity)
        self.quantity_spinbox.setMinimum(1)
        self.quantity_spinbox.valueChanged.connect(self.update_quantity)
        self.layout.addWidget(self.quantity_spinbox)

        self.price_label = QLabel(f"{product['price'] * quantity:.2f} RON")
        self.layout.addWidget(self.price_label)

    def update_quantity(self):
        self.product["quantity"] = self.quantity_spinbox.value()
        self.price_label.setText(f"{self.product['price'] * self.product['quantity']:.2f} RON")
        self.update_callback()

    def refresh_spinner(self, new_spinner_value):
        self.quantity_spinbox.setValue(new_spinner_value)

class CheckView(QWidget):
    products = {} # key - product_id, value - {product_name, quantity, price, etc...}
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.order_state: OrderPageState = OrderPageState.instance()

        self.load_view()

        self.order_state.product_added.connect(self.add_product)

    def load_view(self):
        # Creare layout principal
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Creare widget pentru lista de produse
        self.product_list_widget = QWidget()
        self.product_list_layout = QVBoxLayout()
        self.product_list_widget.setLayout(self.product_list_layout)
        self.main_layout.addWidget(self.product_list_widget)

        self.setStyleSheet(f"background-color: {Colors.MEDIUM_GRAY_2};border-radius: 4px;")
        self.setLayout(self.main_layout)

    def add_product(self, table_id, product):
        try:
            if product['id'] == -1:
                return
            if product['id'] in self.products:
                self.products[product['id']]['quantity'] += 1
                self.products[product['id']]['widget'].refresh_spinner(self.products[product['id']]['quantity'])
            else:
                self.products[product['id']] = {}
                self.products[product['id']]['quantity'] = 1
                self.products[product['id']]['price'] = product['price']
                self.products[product['id']]['recipe_id'] = product['recipe_id']
                self.products[product['id']]['name'] = product['name']
                product_widget = ProductWidget(product, self.products[product['id']]['quantity'], self.update_total)
                self.products[product['id']]['widget'] = product_widget
                self.product_list_layout.addWidget(product_widget)
            self.update_total()
        except Exception as e:
            print(f"[Error] Product was not added in check ({e})")


    def update_total(self):
        total = sum(p['price'] * p['quantity'] for p in self.products)
        self.total_label.setText(f"Total: {total:.2f} RON")