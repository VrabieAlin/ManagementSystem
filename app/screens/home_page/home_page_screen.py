from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen

from app.screens.home_page.view.navbar_view import NavbarView
from app.screens.home_page.view.restaurant_view import RestaurantView
from app.screens.home_page.view.sidebar_view import SidebarView


class HomePageScreen(Screen):

    def __init__(self, **kwargs):
        super(HomePageScreen, self).__init__(**kwargs)
        self.loadViews()

    def loadViews(self):
        #TODO: fix those layouts to be placed where they need to be
        float_layout = FloatLayout()
        print(float_layout.height)
        print(1-200/float_layout.height)
        # navbar = NavbarView(size_hint=(1, None), height=200, pos_hint={'top': 1})
        # sidebar = SidebarView(size_hint=(None, 1), width=200, pos_hint={'right': 1, 'top': 1})
        # restaurant_view = RestaurantView(size_hint=(None, None),
        #                                  size=(float_layout.width - sidebar.width, float_layout.height - 200),
        #                                  pos=(0, 0))
        # float_layout.add_widget(navbar)
        # float_layout.add_widget(sidebar)
        # float_layout.add_widget(restaurant_view)

        self.add_widget(float_layout)
