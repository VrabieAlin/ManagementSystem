
from functools import partial

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QPushButton, QGridLayout, QSizePolicy, QVBoxLayout

from app.screens.order_page.model.db_loader import OrderDB
from app.screens.order_page.view.elements.widgets.product_cart.product_card import ProductCardContainer
from app.state.order_page_state import OrderPageState
from app.utils.constants import Colors


class ProductsMenuView(QWidget):
    max_cols = 4
    max_rows = 3
    products_pages = []
    def __init__(self, main_window, order_db: OrderDB=None):
        super().__init__()
        self.main_window = main_window
        self.order_db: OrderDB = order_db
        self.order_state: OrderPageState = OrderPageState.instance()

        self.load_logic()
        self.load_view()

        self.order_state.category_change.connect(self.on_change_category)

    def on_change_category(self):
        self.load_logic()
        self.refresh_products_area()
        self.check_arrows()


    def load_logic(self):
        self.products = self.order_db.get_products()
        self.products_pages = []

        self.current_category_id = self.order_state.context.order_page_state.current_category
        self.current_products_list = self.products[self.current_category_id]

        self.current_products_page = 0 #The product page, on each page contains { max_cols x max_rows } products


        #Crate a pagination for products, on each page contains { max_cols x max_rows } products, last page may have less products
        page_size = (self.max_rows + 1) * (self.max_cols + 1)
        for index in range(0, len(self.current_products_list), page_size):
            page = self.current_products_list[index : index + page_size]
            self.products_pages.append(page)

        #Fill last page with default elements to have same size as the others
        # while len(self.products_pages[-1]) < page_size:
        #     self.products_pages[-1].append(Product(-1, " ", 0, " ", -1, -1, -1))


    def load_view(self):
        self.main_layout = self.create_layout_layout()
        self.products_area = self.create_products_area_layout()  # Area with products to be selected
        self.left_arrow = self.create_left_arraw_widget()  # Left arrow button
        self.right_arrow = self.create_right_arrow_widget()  # Right arrow button

        self.positioning_elements()
        self.check_arrows()

        self.setLayout(self.main_layout)

    def create_layout_layout(self):
        main_layout = QGridLayout()
        main_layout.setContentsMargins(0, 0, 10, 10)
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
        self.products_area = QGridLayout()
        self.products_area.setContentsMargins(0, 0, 0, 0)
        self.products_area.setSpacing(10)

        self.refresh_products_area()

        self.products_area.setColumnStretch(0, 1)
        self.products_area.setColumnStretch(1, 1)
        self.products_area.setColumnStretch(2, 1)
        self.products_area.setColumnStretch(3, 1)
        self.products_area.setColumnStretch(4, 1)

        self.products_area.setRowStretch(0, 1)
        self.products_area.setRowStretch(1, 1)
        self.products_area.setRowStretch(2, 1)
        self.products_area.setRowStretch(3, 1)

        # self.setStyleSheet(f"""
        #             QPushButton {{
        #                 background-color: {Colors.SOFT_BLUE};
        #                 color: {Colors.WHITE};
        #                 border: 1px solid {Colors.SOFT_BLUE};
        #                 border-radius: 5px;
        #                 padding: 10px 20px;
        #                 font-size: 20px;
        #                 font-weight: bold;
        #             }}
        #             """)

        return self.products_area

    def create_left_arraw_widget(self):
        button = QPushButton("<<")
        button.setStyleSheet(f"""
                                QPushButton {{
                                    background-color: {Colors.SOFT_BLUE};
                                    color: {Colors.WHITE};
                                    border: 1px solid {Colors.SOFT_BLUE};
                                    border-radius: 5px;
                                    padding: 10px 20px;
                                    font-size: 24px;
                                    font-weight: bold;  
                                }}
                            """)

        button.clicked.connect(partial(self.move_page, "left"))
        button.setFixedSize(350, 70)
        button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        # Create a layout to hold the button and set its alignment to center
        button_layout = QVBoxLayout()
        button_layout.addWidget(button, 0, Qt.AlignmentFlag.AlignCenter)

        # Set the layout to the parent widget
        parent_widget = QWidget()
        parent_widget.setLayout(button_layout)

        return parent_widget

    def create_right_arrow_widget(self):
        button = QPushButton(">>")
        button.setStyleSheet(f"""
                                QPushButton {{
                                    background-color: {Colors.SOFT_BLUE};
                                    color: {Colors.WHITE};
                                    border: 1px solid {Colors.SOFT_BLUE};
                                    border-radius: 5px;
                                    padding: 10px 20px;
                                    font-size: 24px;
                                    font-weight: bold;  
                                }}
                            """)
        button.clicked.connect(partial(self.move_page, "right"))
        button.setFixedSize(350, 70)
        button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        # Create a layout to hold the button and set its alignment to center
        button_layout = QVBoxLayout()
        button_layout.addWidget(button, 0, Qt.AlignmentFlag.AlignCenter)

        # Set the layout to the parent widget
        parent_widget = QWidget()
        parent_widget.setLayout(button_layout)

        return parent_widget

    def move_page(self, direction):
        if direction == 'right' and self.current_products_page < len(self.products_pages):
            self.current_products_page += 1
        if direction == 'left' and self.current_products_page > 0:
            self.current_products_page -= 1
        self.check_arrows()
        self.refresh_products_area()

    def positioning_elements(self):
        self.main_layout.addLayout(self.products_area, 0, 0, 1, 2)
        self.main_layout.addWidget(self.left_arrow, 1, 0, 1, 1)
        self.main_layout.addWidget(self.right_arrow, 1, 1, 1, 1)

        self.main_layout.setRowStretch(0, 10)
        self.main_layout.setRowStretch(1, 1) #TO DO: Verific daca trebuie pusa o sageata, daca nu, o scot de tot, daca trebuie pusa doar o sageata o pun pe intregul spatiu, daca trebuie amandoua le pun pe jumate jumate (cum e acum)

    def check_arrows(self):
        left_arrow_on = False
        if self.current_products_page != 0 and len(self.products_pages) > 1 :
            self.left_arrow.show()
            left_arrow_on = True
        else:
            self.left_arrow.hide()
            left_arrow_on = False

        right_arrow_on = False
        if self.current_products_page != (len(self.products_pages) - 1)  and len(self.products_pages) > 1 :
            self.right_arrow.show()
            right_arrow_on = True
        else:
            self.right_arrow.hide()
            right_arrow_on = False

        if left_arrow_on == False and right_arrow_on == False:
            self.main_layout.setRowStretch(1, 0)
        else:
            self.main_layout.setRowStretch(1, 1)
            self.main_layout.setColumnStretch(0, 1)
            self.main_layout.setColumnStretch(1, 1)


    def refresh_products_area(self):
        print(f"Noua categorie de unde trebuie sa incarc produsele este categoria "
              f"{self.order_state.context.order_page_state.current_category}")

        self.clear_grid(self.products_area)

        current_row = 0
        current_col = 0

        if len(self.products_pages) == 0:
            return

        for product in self.products_pages[self.current_products_page]:

            product_button = ProductCardContainer(product)

            product_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

            product_button.product_card.clicked.connect(partial(self.order_state.add_product_to_basket,
                                                     (self.order_state.context.order_page_state.table_id, product)))# TO DO ADD SEMNAL SPRE CHECK SA ADD PRODUCT

            self.products_area.addWidget(product_button, current_row, current_col)
            current_col += 1
            if current_col > self.max_cols:
                current_col = 0
                current_row += 1
            if current_row > self.max_rows:
                break

    def clear_grid(self, grid):
        # Iterăm prin toate elementele din QGridLayout și le eliminăm
        while grid.count():
            item = grid.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()


