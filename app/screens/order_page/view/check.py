from PySide6.QtWidgets import QScrollArea, QVBoxLayout, QHBoxLayout, QWidget, QLabel
from PySide6.QtCore import Qt
from app.utils.constants import Colors
from app.state.order_page_state import OrderPageState
from app.screens.order_page.view.elements.widgets.product_widget import ProductWidget

class CheckView(QWidget):
    products = {}  # key - product_id, value - {product_name, quantity, price, etc...}

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.order_state: OrderPageState = OrderPageState.instance()
        self.load_view()

        self.order_state.product_added.connect(self.add_product)
        self.setStyleSheet(f"background-color: {Colors.LIGHT_GRAY}; border: 0; border-radius: 5;")

    def load_view(self):
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(10, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.create_header()
        self.create_scroll_area()
        self.create_total_label()

        self.setLayout(self.main_layout)

    def create_header(self):
        self.header_widget = QWidget()
        self.header_layout = QHBoxLayout()
        self.header_widget.setLayout(self.header_layout)
        self.header_widget.setStyleSheet(
            "background-color: #2C2C2C; border-radius: 5; border-bottom-left-radius: 0; border-bottom-right-radius: 0")

        header_style = "color: #FFFFFF; font-size: 18px; font-weight: bold; font-family: Arial, sans-serif;"

        self.product_name_header = QLabel("Produs")
        self.product_name_header.setStyleSheet(header_style)
        self.header_layout.addWidget(self.product_name_header, 1)

        self.quantity_header = QLabel("Cantitate")
        self.quantity_header.setStyleSheet(header_style)
        self.quantity_header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.header_layout.addWidget(self.quantity_header, 1)

        self.price_header = QLabel("Preț")
        self.price_header.setStyleSheet(header_style)
        self.price_header.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.header_layout.addWidget(self.price_header, 1)

        self.main_layout.addWidget(self.header_widget)

    def create_scroll_area(self):
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.main_layout.addWidget(self.scroll_area)

        self.product_list_widget = QWidget()
        self.product_list_widget.setStyleSheet("border-radius: 0;")
        self.product_list_widget.setContentsMargins(0, 0, 0, 0)

        self.product_list_layout = QVBoxLayout()
        self.product_list_layout.setContentsMargins(0, 0, 0, 0)
        self.product_list_layout.setSpacing(0)
        self.product_list_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.product_list_widget.setLayout(self.product_list_layout)
        self.scroll_area.setWidget(self.product_list_widget)

    def create_total_label(self):
        self.total_label = QLabel("Total: 0.00 RON")
        self.total_label.setStyleSheet(
            "color: black; font-size: 20px; font-weight: bold; padding: 10px; margin-bottom: 10px;")
        self.main_layout.addWidget(self.total_label)

    def add_product(self, table_id, product):
        try:
            if product['id'] == -1:
                return
            if product['id'] in self.products:
                self.products[product['id']]['quantity'] += 1
                self.products[product['id']]['widget'].refresh_spinner(self.products[product['id']]['quantity'])
            else:
                self.products[product['id']] = {
                    'quantity': 1,
                    'price': product['price'],
                    'name': product['name'],
                    'recipe_id': product['recipe_id'],
                }
                product_widget = ProductWidget(product, self.products[product['id']]['quantity'], self.update_product)

                # Apply zebra striping
                if len(self.products) % 2 == 0:
                    product_widget.setStyleSheet("background-color: #F5F5F5;")  # Light color
                else:
                    product_widget.setStyleSheet("background-color: #E0E0E0;")  # Darker color

                self.products[product['id']]['widget'] = product_widget
                self.product_list_layout.addWidget(product_widget)
            self.update_total()
        except Exception as e:
            print(f"[Error] Product was not added in check ({e})")

    def update_total(self):
        total = sum(p['price'] * p['quantity'] for p in self.products.values())
        self.total_label.setText(f"Total: {total:.2f} RON")

    def update_product(self, product_id, new_quantity):
        self.products[product_id]['quantity'] = new_quantity
        self.update_total()