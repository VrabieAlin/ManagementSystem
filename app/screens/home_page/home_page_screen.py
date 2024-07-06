import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QGridLayout

from app.screens.home_page.view.navbar_view import NavbarView
from app.screens.home_page.view.restaurant_view import RestaurantView
from app.screens.home_page.view.sidebar_view import SidebarView


class HomePageScreen(QWidget):

    def __init__(self, **qtargs):
        super().__init__(**qtargs)
        self.loadViews()

    def loadViews(self):

        grid_layout = QGridLayout()

        #Elements:
        navbar = NavbarView()
        scroll_bar = SidebarView()
        restaurant_view = RestaurantView()

        grid_layout.addWidget(navbar, 0, 0, 1, 2)
        grid_layout.addWidget(restaurant_view, 1, 0)
        grid_layout.addWidget(scroll_bar, 1, 1)

        grid_layout.setColumnStretch(0, 5)
        grid_layout.setColumnStretch(1, 1)

        grid_layout.setRowStretch(0, 1)
        grid_layout.setRowStretch(1, 5)

        self.my_layout = grid_layout

    def getLayout(self):
        return self.my_layout


