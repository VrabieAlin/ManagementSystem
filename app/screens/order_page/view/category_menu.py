#Layout categoriile mari de produse

from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QFrame
from PySide6.QtCore import Qt

from app.utils.constants import Colors, BorderType, Texts, InputType
from app.utils.css_utils import CSSUtils
from app.utils.widgets.input_modal import InputModal
from app.utils.widgets.Labels.custom_lable_1 import CustomLabel1
from app.utils.widgets.menu_modal import MenuModal
from app.utils.widgets.modal import Modal
from app.utils.widgets.widgets_utils import WidgetUtils
from app.state.state_manager import StateManager

class CategoryMenuView(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.load_view()

    def load_view(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        item = QWidget()

        main_layout.addWidget(item)
        self.setStyleSheet("background-color: green; border: 2px solid blue;")
        self.setLayout(main_layout)