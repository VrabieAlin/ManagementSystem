from PySide6.QtWidgets import QWidget, QGridLayout

from app.screens.home_page.view.navbar_view import NavbarView
from app.screens.home_page.view.restaurant_view import RestaurantView
from app.screens.home_page.view.sidebar_view import SidebarView

class OrderPage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
