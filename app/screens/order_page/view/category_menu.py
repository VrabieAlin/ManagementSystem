# app/screens/order_page/view/category_menu.py

from functools import partial

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QGridLayout, QFrame, QHBoxLayout, QScrollArea, QSizePolicy, QPushButton
from PySide6.QtGui import QFont

from app.screens.order_page.model.db_loader import OrderDB
from app.screens.order_page.view.elements.Buttons.arrow_button import ArrowButton
from app.state.order_page_state import OrderPageState
from app.utils.widgets.buttons.main_button import PrimaryButton
from app.utils.widgets.custom_scroll_area import CustomScrollArea
from app.utils.constants import Colors

def calculate_total_pages(elements_count):
    if elements_count <= 7:
        return 1
    else:
        # Prima pagină are 7 elemente
        remaining_elements = elements_count - 7
        # Fiecare pagină ulterioară are 6 elemente
        additional_pages = (remaining_elements + 5) // 6  # Folosim (n + (m-1)) // m pentru a calcula numărul de pagini
        return 1 + additional_pages

class CategoryMenuView(QWidget):
    def __init__(self, main_window, order_db: OrderDB=None):
        super().__init__()
        self.main_window = main_window
        self.order_db = order_db
        self.order_page_state: OrderPageState = OrderPageState.instance()

        self.categories = self.order_db.load_categories()
        self.current_page = 0
        self.elements_per_page = 6

        self.load_view()

    def load_view(self):
        self.main_layout = self.create_layout_layout()
        self.categories_widget = self.create_categories_widget() # List of category

        self.positioning_elements()

        self.setLayout(self.main_layout)

    def create_layout_layout(self) -> QGridLayout:
        main_layout = QGridLayout()
        main_layout.setContentsMargins(0, 0, 10, 0)
        main_layout.setSpacing(0)

        return main_layout

    def create_categories_widget(self) -> QWidget:
        self.categories_widget = QWidget()
        self.categories_layout = QGridLayout()
        self.categories_layout.setContentsMargins(0, 0, 0, 0)
        self.categories_layout.setSpacing(5)
        self.categories_widget.setLayout(self.categories_layout)

        self.update_categories_layout()

        return self.categories_widget

    def update_categories_layout(self):
        self.clear_layout(self.categories_layout)

        button_style = f"""
            QPushButton {{
                background-color: {Colors.SOFT_BLUE};
                border: 1px solid {Colors.SOFT_BLUE};
                color: {Colors.WHITE};
                border-radius: 5px;
                padding: 10px;
            }}
        """
        font = QFont("Arial", 20)


        total_pages = calculate_total_pages(len(self.categories))

        if self.current_page == 0:
            categories_to_display = self.categories[:7]
        else:
            start_index = (self.current_page - 1) * self.elements_per_page + 7
            end_index = start_index + self.elements_per_page
            categories_to_display = self.categories[start_index:end_index]

        if self.current_page > 0:
            back_button = QPushButton("<<")
            back_button.setStyleSheet(button_style)
            back_button.setFont(font)
            back_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            back_button.clicked.connect(self.show_previous_page)
            self.categories_layout.addWidget(back_button, 1, 0)
            column_offset = 1
        else:
            column_offset = 0

        for i, category in enumerate(categories_to_display):
            row = i // 4
            if row == 0 and column_offset == 1:
                col = i % 4
            else:
                col = (i + column_offset) % 4
            button = QPushButton(category.name)
            button.setStyleSheet(button_style)
            button.setFont(font)
            button.clicked.connect(partial(self.order_page_state.change_category, category.id))
            button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            self.categories_layout.addWidget(button, row, col)

        if self.current_page < total_pages - 1:
            next_button = QPushButton(">>")
            next_button.setStyleSheet(button_style)
            next_button.setFont(font)
            next_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            next_button.clicked.connect(self.show_next_page)
            self.categories_layout.addWidget(next_button, 1, 3)

        for i in range(8):
            row = i // 4
            col = i % 4
            if self.categories_layout.itemAtPosition(row, col) is None:
                empty_button = QPushButton("")
                empty_button.setStyleSheet(button_style)
                empty_button.setFont(font)
                empty_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
                empty_button.setEnabled(False)
                self.categories_layout.addWidget(empty_button, row, col)
    def show_previous_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.update_categories_layout()

    def show_next_page(self):
        if (self.current_page + 1) * self.elements_per_page < len(self.categories):
            self.current_page += 1
            self.update_categories_layout()

    def clear_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def positioning_elements(self):
        self.main_layout.addWidget(self.categories_widget)