from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QGridLayout, QVBoxLayout, QPushButton, \
    QStyleOption, QStyle

from app.screens.order_page.view.elements.widgets.check_row.notes import NotesEditor
from app.screens.order_page.view.elements.widgets.check_row.selected_product_menu import SelectedProductMenu
from app.screens.order_page.view.elements.widgets.check_row.spin_widget import SpinWidget
from PySide6.QtCore import Qt

import random
import string

from app.utils.constants import Colors
from app.state.order_page_state import OrderPageState, BasketProduct


class ProductWidget(QPushButton):
    def __init__(self, basket_product, parent=None):
        super().__init__(parent)
        self.basket_product: BasketProduct = basket_product
        self.selected_product_menu = None
        self.notes_editor = None

        self.selected = False
        self.order_page_state: OrderPageState = OrderPageState.instance()
        random_id = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        self.setObjectName(
            f"product_widget_{basket_product.product.id}_{random_id}")  # fiecare nume trebuie sa aiba un nume unic pentru a fi identificat unic

        self.setContentsMargins(0, 0, 0, 0)

        self.load_view()

    def paintEvent(self, pe):
        o = QStyleOption()
        o.initFrom(self)
        p = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, o, p, self)

    def reload_element(self, basket_product):

        #--------Close phase---------
        self.basket_product: BasketProduct = basket_product
        self.layout.removeWidget(self.name_label)
        self.layout.removeWidget(self.parent_spin)
        self.layout.removeWidget(self.price_label)
        self.name_label.deleteLater()
        self.parent_spin.deleteLater()
        self.price_label.deleteLater()

        if self.selected: #Fortam selectarea din nou
            self.deselect()
            self.selected = True

        #--------Open phase---------
        self.setup_name_label()
        self.setup_spin_widget()
        self.setup_price_label()

        if self.selected:
            self.select()

    def load_view(self):
        # self.setStyleSheet(f"""
        #                 border-radius: 0;
        #             """)

        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(5, 5, 5, 5)
        self.layout.setSpacing(0)

        self.setFixedHeight(60)

        self.setLayout(self.layout)

        self.setup_name_label()
        self.setup_spin_widget()
        self.setup_price_label()

    def setup_name_label(self):
        self.name_label = QLabel(self.basket_product.product.name)
        self.name_label.setStyleSheet("font-size: 24px; color: #000000; padding: 5px;")
        self.layout.addWidget(self.name_label, 1)

    def setup_spin_widget(self):
        self.parent_spin = QWidget()
        self.parent_layout = QGridLayout(self.parent_spin)
        self.parent_layout.setContentsMargins(0, 0, 0, 0)
        self.parent_layout.setSpacing(0)

        self.spin_widget = SpinWidget(self.basket_product, self.update_quantity)
        self.spin_widget.setAutoFillBackground(True)
        self.spin_widget.setParent(self.parent_spin)

        self.parent_layout.addWidget(self.spin_widget, 1, 1)

        self.layout.addWidget(self.parent_spin, 1)

    def setup_price_label(self):
        self.price_label = QLabel(f"{self.basket_product.product.price * self.basket_product.quantity:.2f} RON")
        self.price_label.setStyleSheet("font-size: 24px; color: #000000; padding: 0 5px;")
        self.price_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
        self.layout.addWidget(self.price_label, 1)

    def update_quantity(self, new_quantity):
        self.basket_product.quantity = new_quantity
        self.price_label.setText(f"{self.basket_product.product.price * self.basket_product.quantity:.2f} RON")
        self.order_page_state.update_check((str(self.basket_product.table_id), self.basket_product))

    def update_description(self, new_description):
        self.basket_product.notes = new_description
        self.order_page_state.update_check((str(self.basket_product.table_id), self.basket_product))

    def refresh_spinner(self, new_spinner_value):
        self.spin_widget.set_value(new_spinner_value)

    def select(self):

        widget_name = self.objectName()
        self.old_style = self.styleSheet()

        self.setStyleSheet(f"""
                        #{widget_name} {{
                            border: 1px solid {Colors.SOFT_BLUE};
                            border-radius: 5px;
                            
                        }}
                        QWidget {{
                            background-color: {Colors.SOFT_BLUE_2};
                        }}
                        """)

        self.selected = True

        if self.selected_product_menu is None:
            callbacks = {
                "edit_description": self.update_description,
                "modify_number": self.update_quantity,
            }
            self.selected_product_menu = SelectedProductMenu(self.basket_product, callbacks, self.deselect, self)
            self.selected_product_menu.move(self.mapToGlobal(self.rect().topRight()))
            self.selected_product_menu.show()

        if self.basket_product.notes != "":
            if self.notes_editor is None:
                self.notes_editor = NotesEditor(self.basket_product, self.update_description, self.deselect, self)
                self.notes_editor.move(self.mapToGlobal(self.rect().bottomLeft()))
                self.notes_editor.show()


    def deselect(self):
        self.setStyleSheet(self.old_style)
        self.selected = False

        # Hide and delete the selected product menu
        if self.selected_product_menu is not None:
            self.selected_product_menu.close()
            self.selected_product_menu = None

        if self.notes_editor is not None:
            self.notes_editor.close()
            self.notes_editor = None

class ProductRawContainer(QPushButton):
    def __init__(self, basket_product, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)  # Set margin-top to 10px
        self.product_card = ProductWidget(basket_product, self)

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
