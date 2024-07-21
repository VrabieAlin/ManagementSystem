from PySide6.QtWidgets import QWidget, QGridLayout
from PySide6.QtCore import Qt

from app.screens.order_page.view.top_bar import TopBarView
from app.screens.order_page.view.check import CheckView
from app.screens.order_page.view.category_menu import CategoryMenuView
from app.screens.order_page.view.products_menu import ProductsMenuView
from app.screens.order_page.view.option_menu import OptionsView

class OrderPage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setLayout(self.load_view())

    def load_view(self):
        main_layout = QGridLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)

        #-----Elements-----
        top_bar = TopBarView(main_window=self.main_window)
        category_menu = CategoryMenuView(main_window=self.main_window)
        products_menu = ProductsMenuView(main_window=self.main_window)
        check = CheckView(main_window=self.main_window)
        options = OptionsView(main_window=self.main_window)

        #-----Arangements-----
        main_layout.addWidget(top_bar, 0, 0, 1, 2)
        main_layout.addWidget(check, 2, 0, 1, 1)
        main_layout.addWidget(category_menu, 1, 0, 1, 2)
        main_layout.addWidget(products_menu, 2, 1, 1, 1)
        main_layout.addWidget(options, 3, 0, 1, 2)

        #-----Resizing-----
        main_layout.setRowStretch(0, 2)
        main_layout.setRowStretch(1, 10)
        main_layout.setRowStretch(2, 70)
        main_layout.setRowStretch(3, 18)

        main_layout.setColumnStretch(0, 40)
        main_layout.setColumnStretch(1, 60)

        return main_layout



