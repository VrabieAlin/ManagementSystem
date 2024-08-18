from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QSpinBox, QLabel
from PySide6.QtCore import Qt

from app.screens.order_page.view.elements.widgets.check_row.spin_box_widget import CustomSpinBox
from app.utils.constants import Colors


class SpinWidget(QWidget):
    def __init__(self, basket_product, update_callback):
        super().__init__()
        self.update_callback = update_callback
        self.basket_product = basket_product
        #self.setStyleSheet("background-color: white; border-radius: 5px;")
        self.load_view()


    def load_view(self):
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.layout.addStretch(1)
        self.setup_decrement_button()
        self.setup_quantity_spinbox()
        self.setup_increment_button()
        self.layout.addStretch(1)

        self.setLayout(self.layout)

    def setup_decrement_button(self):
        self.decrement_button = QPushButton("-")
        self.decrement_button.setFixedSize(40, 40)
        self.decrement_button.setStyleSheet(f"""
                                QPushButton 
                                {{ 
                                    background-color: {Colors.SOFT_BLUE_2};
                                    border: 1px solid {Colors.SOFT_BLUE};
                                    color: white;
                                    border-top-left-radius: 5px;
                                    border-bottom-left-radius: 5px;
                                    font-size: 24px;
                                }}
                                """)

        self.decrement_button.clicked.connect(self.decrement_quantity)
        self.layout.addWidget(self.decrement_button)

    def setup_quantity_spinbox(self):
        self.quantity_spinbox = CustomSpinBox(self.basket_product, self.update_callback)
        self.layout.addWidget(self.quantity_spinbox)

    def mousePressEvent(self, event):
        print("Mouse pressed2")
    def setup_increment_button(self):
        self.increment_button = QPushButton("+")
        self.increment_button.setFixedSize(40, 40)
        self.increment_button.setStyleSheet(f"""
                        QPushButton 
                        {{ 
                            background-color: {Colors.SOFT_BLUE_2};
                            border: 1px solid {Colors.SOFT_BLUE};
                            color: white;
                            border-bottom-right-radius: 5px;
                            border-top-right-radius: 5px;
                            font-size: 24px;
                        }}
                        """)
        self.increment_button.clicked.connect(self.increment_quantity)
        self.layout.addWidget(self.increment_button)

    def increment_quantity(self):
        self.quantity_spinbox.setValue(self.quantity_spinbox.value() + 1)

    def decrement_quantity(self):
        if self.quantity_spinbox.value() > 1:
            self.quantity_spinbox.setValue(self.quantity_spinbox.value() - 1)

    def update_quantity(self):
        self.update_callback(self.quantity_spinbox.value())

    def set_value(self, value):
        self.quantity_spinbox.setValue(value)

