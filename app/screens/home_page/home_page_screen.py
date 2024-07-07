from PySide6.QtWidgets import QWidget, QGridLayout

from app.screens.home_page.view.navbar_view import NavbarView
from app.screens.home_page.view.restaurant_view import RestaurantView
from app.screens.home_page.view.sidebar_view import SidebarView


class HomePageScreen(QWidget):

    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setLayout(self.loadViews())

    def loadViews(self):
        grid_layout = QGridLayout()
        grid_layout.setHorizontalSpacing(0)
        grid_layout.setVerticalSpacing(0)

        # Init views
        navbar = NavbarView()
        side_bar = SidebarView(self.main_window)
        restaurant_view = RestaurantView()

        grid_layout.addWidget(navbar, 0, 0, 1, 2)
        grid_layout.addWidget(restaurant_view, 1, 0)
        grid_layout.addWidget(side_bar, 1, 1)

        grid_layout.setColumnStretch(0, 5)
        grid_layout.setColumnStretch(1, 1)

        grid_layout.setRowStretch(0, 1)
        grid_layout.setRowStretch(1, 6)

        grid_layout.setRowMinimumHeight(0, 100)
        grid_layout.setColumnMinimumWidth(1, 100)

        return grid_layout
