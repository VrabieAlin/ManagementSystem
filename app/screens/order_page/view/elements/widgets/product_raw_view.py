from PySide6 import QtCore
from PySide6.QtGui import QTouchEvent, QPainter
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QSizePolicy, QGridLayout, QVBoxLayout, QPushButton, \
    QStyleOption, QStyle
from app.screens.order_page.view.elements.widgets.spin_widget import SpinWidget
from PySide6.QtCore import Qt, Signal, QEvent

import random
import string

from app.utils.constants import Colors


class ProductWidget(QPushButton):
    def __init__(self, product, quantity, update_callback, parent=None):
        super().__init__(parent)
        self.product = product

        self.selected = False
        random_id = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        self.setObjectName(
            f"product_widget_{product.id}_{random_id}")  # fiecare nume trebuie sa aiba un nume unic pentru a fi identificat unic

        self.setStyleSheet(f"""
                        #{self.objectName()} {{
                            border: 1px solid {Colors.SOFT_BLUE};
                            background-color: {Colors.SOFT_BLUE_2};
                        }}""")
        self.update_callback = update_callback
        self.quantity = quantity
        self.setContentsMargins(0, 0, 0, 0)

        self.load_view()

    def paintEvent(self, pe):
        o = QStyleOption()
        o.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PE_Widget, o, p, self)

    def load_view(self):
        # self.setStyleSheet(f"""
        #                 border-radius: 0;
        #             """)

        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.setFixedHeight(60)

        self.setLayout(self.layout)

        self.setup_name_label()
        self.setup_spin_widget()
        self.setup_price_label()

    def setup_name_label(self):
        self.name_label = QLabel(self.product.name)
        self.name_label.setStyleSheet("font-size: 24px; color: #000000; padding: 5px;")
        self.layout.addWidget(self.name_label, 1)

    def setup_spin_widget(self):
        self.parent_spin = QWidget()
        self.parent_layout = QGridLayout(self.parent_spin)
        self.parent_layout.setContentsMargins(0, 0, 0, 0)
        self.parent_layout.setSpacing(0)

        self.spin_widget = SpinWidget(self.quantity, self.update_quantity)
        self.spin_widget.setAutoFillBackground(True)
        self.spin_widget.setParent(self.parent_spin)

        self.parent_layout.addWidget(self.spin_widget, 1, 1)

        self.layout.addWidget(self.parent_spin, 1)

    def setup_price_label(self):
        self.price_label = QLabel(f"{self.product.price * self.quantity:.2f} RON")
        self.price_label.setStyleSheet("font-size: 24px; color: #000000; padding: 0 5px;")
        self.price_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.layout.addWidget(self.price_label, 1)

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
        self.price_label.setText(f"{self.product.price * self.quantity:.2f} RON")
        self.update_callback(self.product.id, new_quantity)

    def refresh_spinner(self, new_spinner_value):
        self.spin_widget.set_value(new_spinner_value)

    def select(self):

        widget_name = self.objectName()
        self.old_style = self.styleSheet()

        self.setStyleSheet(f"""
                        #{widget_name} {{
                            border: 1px solid {Colors.SOFT_BLUE};
                            background-color: {Colors.SOFT_BLUE_2};
                        }}""")
        self.selected = True

    def deselect(self):
        self.setStyleSheet(self.old_style)
        self.selected = False

class ProductRawContainer(QPushButton):
    def __init__(self, product, quantity, update_callback, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)  # Set margin-top to 10px
        self.product_card = ProductWidget(product, quantity, update_callback, self)

        self.layout.addWidget(self.product_card)
        self.setFixedHeight(60)
        self.selected = False
        self.setLayout(self.layout)

    def select(self):
        self.product_card.select()
        self.selected = True

    def deselect(self):
        self.product_card.deselect()
        self.selected = False
