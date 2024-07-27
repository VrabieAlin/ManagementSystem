
from PySide6.QtWidgets import QWidget, QPushButton, QGridLayout, QFrame, QHBoxLayout, QLabel, QSizePolicy
from functools import partial

from app.utils.widgets.Buttons.main_button import PrimaryButton
from app.utils.widgets.custom_scroll_area import CustomScrollArea
from app.screens.order_page.view.elements.Buttons.arrow_button import ArrowButton
from app.screens.order_page.model.db_loader import OrderDB
from app.utils.constants import Colors



class ProductsMenuView(QWidget):
    def __init__(self, main_window, order_db: OrderDB=None, order_page=None):
        super().__init__()
        self.main_window = main_window
        self.order_db = order_db
        self.order_page = order_page

        self.products = self.order_db.get_products()
        self.load_view()

    def load_view(self):
        self.main_layout = self.create_layout_layout()
        self.products_area = self.create_products_area_layout()  # Area with products to be selected
        self.left_arrow = self.create_left_arraw_widget()  # Left arrow button
        self.right_arrow = self.create_right_arrow_widget()  # Right arrow button

        self.positioning_elements()

        self.setLayout(self.main_layout)

    def create_layout_layout(self):
        main_layout = QGridLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(5)

        return main_layout

    def get_number_of_widgets(self, layout):
        count = 0
        for i in range(layout.count()):
            item = layout.itemAt(i)
            if item.widget() is not None:
                count += 1
        return count
    def create_products_area_layout(self): #5 cols x 4 rows
        products_area = QGridLayout()
        products_area.setContentsMargins(0, 0, 0, 0)
        products_area.setSpacing(5)
        max_cols = 4
        max_rows = 3

        current_category_id = self.order_page.order_page_state['current_category']
        current_product_list = self.products[current_category_id]

        current_row = 0
        current_col = 0
        for product in current_product_list:
            product_button = QPushButton(product.name)
            product_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            products_area.addWidget(product_button, current_row, current_col)
            current_col += 1
            if current_col > max_cols:
                current_col = 0
                current_row += 1
            #product_name_label = QLabel(product.name)

        while self.get_number_of_widgets(products_area) < 20:
            empty_button = QPushButton()
            empty_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            products_area.addWidget(empty_button, current_row, current_col)
            current_col += 1
            if current_col > max_cols:
                current_col = 0
                current_row += 1

        products_area.setColumnStretch(0, 1)
        products_area.setColumnStretch(1, 1)
        products_area.setColumnStretch(2, 1)
        products_area.setColumnStretch(3, 1)
        products_area.setColumnStretch(4, 1)

        products_area.setRowStretch(0, 1)
        products_area.setRowStretch(1, 1)
        products_area.setRowStretch(2, 1)
        products_area.setRowStretch(3, 1)

        self.setStyleSheet(f"""
                    QPushButton {{
                        background-color: {Colors.SOFT_BLUE};
                        color: {Colors.WHITE};
                        border: 1px solid {Colors.SOFT_BLUE};
                        border-radius: 4px;
                        padding: 10px 20px;
                        font-size: 20px;
                        font-weight: bold;
                    }}
                    """)

        return products_area

    def create_left_arraw_widget(self):
        button = QPushButton(">>")
        button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        return button

    def create_right_arrow_widget(self):
        button = QPushButton("<<")
        button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        return button

    def positioning_elements(self):
        self.main_layout.addLayout(self.products_area, 0, 0, 1, 2)
        self.main_layout.addWidget(self.right_arrow, 1, 0, 1, 1)
        self.main_layout.addWidget(self.left_arrow, 1, 1, 1, 1)

        self.main_layout.setRowStretch(0, 10)
        self.main_layout.setRowStretch(1, 1) #TO DO: Verific daca trebuie pusa o salgeata, daca nu, o scot de tot, daca trebuie pusa doar o sageata o pun pe intregul spatiu, daca trebuie amandoua le pun pe jumate jumate (cum e acum)

    def load_products(self):
        print(f"Noua categorie de unde trebuie sa incarc produsele este categoria {self.order_page.order_page_state['current_category']}")
    def scroll_direction(self, direction="right"):
        if self.categories_layout.count() > 0:
            # Obține bara de derulare verticală
            scrollbar = self.scroll_area.horizontalScrollBar()

            #Obtin valoarea cu care vreau sa fac scroll (dimensiunea butonului unei categorii)
            scroll_value = self.categories_layout.itemAt(0).widget().width()

            if direction == "right":
                # Calculează noua valoare a scroll-ului
                new_value = scrollbar.value() + scroll_value
                if new_value > scrollbar.maximum():
                    scrollbar.setValue(scrollbar.maximum())
                    self.right_arrow.set_availability(available=False)
                    self.right_arrow.setDown(True)
                    self.left_arrow.set_availability(available=True)
                    self.left_arrow.setDown(False)
                else:
                    scrollbar.setValue(new_value)
                    self.left_arrow.set_availability(available=True)
                    self.left_arrow.setDown(False)
            else:
                # Calculează noua valoare a scroll-ului
                new_value = scrollbar.value() - scroll_value
                if new_value < scrollbar.minimum():
                    scrollbar.setValue(scrollbar.minimum())
                    self.left_arrow.set_availability(available=False)
                    self.left_arrow.setDown(True)
                    self.right_arrow.set_availability(available=True)
                    self.right_arrow.setDown(False)
                else:
                    scrollbar.setValue(new_value)
                    self.right_arrow.set_availability(available=True)
                    self.right_arrow.setDown(False)

