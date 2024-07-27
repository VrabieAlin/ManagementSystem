#Layout categoriile mari de produse

from PySide6.QtWidgets import QWidget, QPushButton, QGridLayout, QFrame, QHBoxLayout
from functools import partial

from app.utils.widgets.buttons.main_button import PrimaryButton
from app.utils.widgets.custom_scroll_area import CustomScrollArea
from app.screens.order_page.view.elements.Buttons.arrow_button import ArrowButton
from app.screens.order_page.model.db_loader import OrderDB

class CategoryMenuView(QWidget):
    def __init__(self, main_window, order_db: OrderDB=None, order_page=None):
        super().__init__()
        self.main_window = main_window
        self.order_db = order_db
        self.order_page = order_page

        self.categories = self.order_db.load_categories()
        self.load_view()

    def load_view(self):
        self.main_layout = self.create_layout_layout()
        self.scroll_area = self.create_scroll_area_widget() #List of category
        self.left_arrow = self.create_left_arraw_widget() #Left arrow button
        self.right_arrow = self.create_right_arrow_widget() #Right arrow button

        self.positioning_elements()
        self.check_arrow_availability()

        self.setLayout(self.main_layout)

    def create_layout_layout(self) -> QGridLayout:
        main_layout = QGridLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(5)

        return main_layout

    def create_scroll_area_widget(self) -> CustomScrollArea:
        # Categories
        button_background_widget = QWidget()
        self.categories_layout = QHBoxLayout(button_background_widget)

        for category in self.categories:
            try:
                category_button = PrimaryButton(category.name)
                category_button.clicked.connect(partial(self.order_page.change_category, category.id))
                self.categories_layout.addWidget(category_button)
            except Exception as e:
                print(f"Categoria {category.name} nu s-a putut initializa ({e})")

        self.categories_layout.addWidget(PrimaryButton("Pizza1"))
        self.categories_layout.addWidget(PrimaryButton("Pizza2"))
        self.categories_layout.addWidget(PrimaryButton("Pizza3"))
        self.categories_layout.addWidget(PrimaryButton("Pizza4"))
        self.categories_layout.addWidget(PrimaryButton("Pizza5"))
        self.categories_layout.addWidget(PrimaryButton("Pizza6"))
        self.categories_layout.addWidget(PrimaryButton("Pizza7"))
        self.categories_layout.addWidget(PrimaryButton("Pizza8"))
        self.categories_layout.addWidget(PrimaryButton("Pizza9"))
        self.categories_layout.addWidget(PrimaryButton("Pizza10"))


        self.categories_layout.addStretch(1)

        # Creează un QScrollArea și setează scroll_content ca widget conținut
        scroll_area = CustomScrollArea()
        scroll_area.setMinimumHeight(120)
        scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        scroll_area.setWidget(button_background_widget)

        return scroll_area

    def create_left_arraw_widget(self):
        # Left arrow
        left_arrow = ArrowButton("<<")
        left_arrow.clicked.connect(partial(self.scroll_direction, direction="left"))

        return left_arrow

    def create_right_arrow_widget(self):
        # Right arrow
        right_arrow = ArrowButton(">>")
        right_arrow.clicked.connect(partial(self.scroll_direction, direction="right"))

        return right_arrow

    def positioning_elements(self):
        self.main_layout.addWidget(self.left_arrow, 0, 0)
        self.main_layout.addWidget(self.scroll_area, 0, 1)
        self.main_layout.addWidget(self.right_arrow, 0, 2)

        self.main_layout.setColumnStretch(0, 1)
        self.main_layout.setColumnStretch(1, 10)
        self.main_layout.setColumnStretch(2, 1)


    def check_arrow_availability(self):
        horizontal_scrollbar = self.scroll_area.horizontalScrollBar()

        can_scroll_left = horizontal_scrollbar.value() > horizontal_scrollbar.minimum()
        can_scroll_right = horizontal_scrollbar.value() < horizontal_scrollbar.maximum()

        if can_scroll_left:
            self.left_arrow.show()
            self.main_layout.setColumnStretch(0, 1)
        else:
            self.left_arrow.hide()
            self.main_layout.setColumnStretch(0, 0)

        if can_scroll_right:
            self.right_arrow.show()
            self.main_layout.setColumnStretch(2, 1)
        else:
            self.right_arrow.hide()
            self.main_layout.setColumnStretch(2, 0)

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
                else:
                    scrollbar.setValue(new_value)
            else:
                # Calculează noua valoare a scroll-ului
                new_value = scrollbar.value() - scroll_value
                if new_value < scrollbar.minimum():
                    scrollbar.setValue(scrollbar.minimum())
                else:
                    scrollbar.setValue(new_value)

            self.check_arrow_availability()

