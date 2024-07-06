from kivy.uix.screenmanager import Screen

from app.custom_widgets.grid_layout import GridLayout
from app.screens.home_page.view.navbar_view import NavbarView
from app.screens.home_page.view.restaurant_view import RestaurantView
from app.screens.home_page.view.sidebar_view import SidebarView


class HomePageScreen(Screen):

    def __init__(self, **kwargs):
        super(HomePageScreen, self).__init__(**kwargs)
        self.loadViews()

    def loadViews(self):
        layout = GridLayout()

        #create views
        navbar = NavbarView(height=200, size_hint_y=None, orientation='horizontal')
        restaurant_view = RestaurantView()
        sidebar = SidebarView(size_hint_x=None, width=350, orientation='vertical')

        layout.add_row([navbar])
        layout.add_row([restaurant_view,sidebar])

        self.add_widget(layout)
