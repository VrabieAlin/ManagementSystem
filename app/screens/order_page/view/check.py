from PySide6.QtWidgets import QScrollArea, QVBoxLayout, QHBoxLayout, QWidget, QLabel
from PySide6.QtCore import Qt

from app.screens.order_page.model.product import Product
from app.utils.constants import Colors, ORDERED_PRODUCT_STATUS as PRODUCT_STATUS
from app.screens.order_page.view.elements.widgets.check_row.product_raw_view import ProductRawContainer, ProductWidget, BasketProduct, OrderPageState

import traceback
import random
import string

class CheckView(QWidget):
    basket_products: dict[str, dict[str, BasketProduct]] = {}  # key - table_id, value - dict[basket_id, BasketProduct]
    basket_products_widgets: dict[str, ProductRawContainer] = {}  # key - basket_id, value - ProductRawContainer (widget for that basket_product_id)
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.selected_product = None

        self.order_state: OrderPageState = OrderPageState.instance()


        self.load_view()
        self.load_basket_products_from_state()

        self.order_state.product_added_signal.connect(self.add_product)
        self.setStyleSheet(f"background-color: {Colors.LIGHT_GRAY}; border: 0; border-radius: 5;")

    def load_view(self):
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(10, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.create_header()
        self.create_scroll_area()
        self.create_total_label()

        #Trebuie sa distrug elementele dupa ce ies de aici?

        self.order_state.reload_check_signal.connect(self.reload_basket_product)

        self.setLayout(self.main_layout)

    def load_basket_products_from_state(self):
        for table_id, basket_products in self.order_state.context['tables_orders'].items():
            for basket_product in basket_products.values():
                if table_id not in self.basket_products:
                    self.basket_products[table_id] = {}
                self.basket_products[table_id][basket_product.basket_id] = BasketProduct.from_dict(basket_product)
                if basket_product.basket_id not in self.basket_products_widgets:
                    product_widget = ProductRawContainer(self.basket_products[table_id][basket_product.basket_id], self)
                    product_widget.product_card.clicked.connect(self.show_hide_item_menu)
                    # Apply zebra striping
                    if len(self.basket_products[table_id]) % 2 == 0:
                        product_widget.setStyleSheet("background-color: #F5F5F5;")  # Light color
                    else:
                        product_widget.setStyleSheet("background-color: #E0E0E0;")  # Darker color
                    self.basket_products_widgets[basket_product.basket_id] = product_widget
                    self.product_list_layout.addWidget(product_widget)  # Add product to the list

        self.update_total()

    def create_header(self):
        self.header_widget = QWidget()
        self.header_layout = QHBoxLayout()
        self.header_widget.setLayout(self.header_layout)
        self.header_widget.setStyleSheet(
            f"background-color: {Colors.SOFT_BLUE}; border-radius: 5; border-bottom-left-radius: 0; border-bottom-right-radius: 0")

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
        self.product_list_widget.setObjectName("scroll_area")
        self.product_list_widget.setStyleSheet(f"""
                                #scroll_area {{
                                    background-color: {Colors.SOFT_BLUE_3};
                                    
                                }} 
                                QWidget {{
                                    border-radius: 0;
                                }}
                            """)

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
            f"background-color: {Colors.SOFT_BLUE_3}; color: black; font-size: 20px; font-weight: bold; padding: 10px; margin-bottom: 10px; border-radius: 5; border-top-left-radius: 0; border-top-right-radius: 0")
        self.main_layout.addWidget(self.total_label)

    def generate_basket_id(self):
        # Lungimea șirului aleator
        lungime = 20

        # Setul de caractere din care se va genera șirul
        caractere = string.ascii_letters + string.digits + string.punctuation

        # Generarea șirului aleator
        sir_random = ''.join(random.choice(caractere) for _ in range(lungime))

        return sir_random

    def add_product(self, table_id, product: Product):
        try:
            if product is None or product.id == -1 or table_id == -1:
                return
            table_id = str(table_id)
            if table_id not in self.basket_products:
                self.basket_products[table_id] = {}

            else:
                basket_id = self.get_basket_id_from_product(product.id)
                if basket_id is not None:
                    self.basket_products[table_id][basket_id].quantity += 1
                    if basket_id in self.basket_products_widgets:
                        self.basket_products_widgets[basket_id].product_card.refresh_spinner(
                            self.basket_products[table_id][basket_id].quantity)
                    else:
                        product_widget = ProductRawContainer(self.basket_products[table_id][basket_id], self)
                        product_widget.product_card.clicked.connect(self.show_hide_item_menu)
                        self.basket_products_widgets[basket_id] = product_widget
                        self.product_list_layout.addWidget(product_widget)
                    self.update_total()
                    return

            #product does not exist as a new product in basket so we add it
            basket_id = self.generate_basket_id()

            self.basket_products[table_id][basket_id] = BasketProduct(basket_id, 1, table_id, PRODUCT_STATUS.NEW, product)

            product_widget = ProductRawContainer(self.basket_products[table_id][basket_id], self)
            product_widget.product_card.clicked.connect(self.show_hide_item_menu)

            #Apply zebra striping
            if len(self.basket_products[table_id]) % 2 == 0:
                product_widget.setStyleSheet("background-color: #F5F5F5;")  # Light color
            else:
                product_widget.setStyleSheet("background-color: #E0E0E0;")  # Darker color

            self.basket_products_widgets[basket_id] = product_widget
            self.product_list_layout.addWidget(product_widget)
            self.update_total()
        except Exception as e:
            print(f"[Error check] Product was not added in check ({e})")
            print(f"[Error check] Stack trace: ({traceback.format_exc()})")

    def update_total(self):
        current_table_id = str(self.order_state.context['order_page_state']['table_id'])
        total = sum(p.product.price * p.quantity for p in self.basket_products[current_table_id].values())
        self.total_label.setText(f"Total: {total} RON")

    def update_product(self, product_id, new_quantity):
        current_table_id = str(self.order_state.context['order_page_state']['table_id'])
        basket_id = self.get_basket_id_from_product(product_id)
        if basket_id is not None:
            self.basket_products[current_table_id][basket_id].quantity = new_quantity
            self.update_total()
        else:
            print(f"[Error check] Could not update product with id {product_id}")


    def get_basket_id_from_product(self, product_id, product_status = PRODUCT_STATUS.NEW):
        try:
            current_table_id = str(self.order_state.context['order_page_state']['table_id'])
            for basket_id, basket_product in self.basket_products[current_table_id].items():
                if basket_product.product.id == product_id and product_status == basket_product.status:
                    return basket_id
        except Exception as e:
            print(f"[Error check] Could not get basket id from product ({e})")
            print(f"[Error check] Stack trace: ({traceback.format_exc()})")
        return None

    def reload_basket_product(self, basket_product):
        table_id = str(basket_product.table_id)

        if table_id not in self.basket_products:
            self.basket_products[table_id] = {}

        if basket_product.basket_id in self.basket_products[table_id]:
            self.basket_products_widgets[basket_product.basket_id].product_card.reload_element(basket_product)
        else:
            self.add_product(basket_product.table_id, basket_product.product)

        self.update_total()

    def show_hide_item_menu(self):
        widget: ProductWidget = self.sender()

        if self.selected_product is not None and self.selected_product != widget:
            self.selected_product.deselect()
        self.selected_product = widget

        if widget.selected == False:
            widget.select()
        else:
            widget.deselect()
            self.selected_product = None
