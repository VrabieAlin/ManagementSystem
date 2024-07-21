#Layout categoriile mari de produse

from PySide6.QtWidgets import QWidget, QPushButton, QGridLayout, QFrame, QHBoxLayout
from functools import partial

from app.utils.widgets.Buttons.main_button import PrimaryButton
from app.utils.widgets.custom_scroll_area import CustomScrollArea
from app.screens.order_page.view.elements.Buttons.arrow_button import ArrowButton
from app.screens.order_page.model.db_loader import OrderDB

class CategoryMenuView(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.order_db = OrderDB(self.main_window)

        self.categories = self.order_db.load_categories()
        self.load_view()

    def load_view(self):
        main_layout = QGridLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(10)

        #Categories
        button_background_widget = QWidget()
        self.categories_layout = QHBoxLayout(button_background_widget)

        for category in self.categories:
            self.categories_layout.addWidget(PrimaryButton(category.name))

        #For testing:
        self.categories_layout.addWidget(PrimaryButton("Pizza 1"))
        self.categories_layout.addWidget(PrimaryButton("Pizza 2"))
        self.categories_layout.addWidget(PrimaryButton("Pizza 3"))
        self.categories_layout.addWidget(PrimaryButton("Pizza 4"))
        self.categories_layout.addWidget(PrimaryButton("Pizza 5"))
        self.categories_layout.addWidget(PrimaryButton("Pizza 6"))
        self.categories_layout.addWidget(PrimaryButton("Pizza 7"))
        self.categories_layout.addWidget(PrimaryButton("Pizza 8"))
        #End of test

        self.categories_layout.addStretch(1)
        # Creează un QScrollArea și setează scroll_content ca widget conținut
        self.scroll_area = CustomScrollArea()
        self.scroll_area.setMinimumHeight(120)
        self.scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        self.scroll_area.setWidget(button_background_widget)

        # Left arrow
        self.left_arrow = ArrowButton("<<", available=False)
        self.left_arrow.clicked.connect(partial(self.scroll_direction, direction="left"))

        #Right arrow
        self.right_arrow = ArrowButton(">>")
        self.right_arrow.clicked.connect(partial(self.scroll_direction, direction="right"))


        main_layout.addWidget(self.left_arrow, 0, 0)
        main_layout.addWidget(self.scroll_area, 0, 1)
        main_layout.addWidget(self.right_arrow, 0, 2)

        main_layout.setColumnStretch(0, 1)
        main_layout.setColumnStretch(1, 10)
        main_layout.setColumnStretch(2, 1)

        #self.setStyleSheet("background-color: green; border: 2px solid blue;")
        self.setLayout(main_layout)

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

