from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.graphics import *

from app.screens.home_page.view.navbar_view import NavbarView
from app.screens.home_page.view.restaurant_view import RestaurantView
from app.screens.home_page.view.sidebar_view import SidebarView


class HomePageScreen(Screen):

    def __init__(self, **kwargs):
        super(HomePageScreen, self).__init__(**kwargs)
        self.loadViews()

    def loadViews(self):
        # Layout principal pe verticală
        main_layout = BoxLayout(orientation='vertical')

        # Navbar care ocupă 15% din înălțime
        navbar = NavbarView(size_hint=(1, 0.15))
        navbar.add_widget(Label())

        # Layout pentru restul conținutului pe axa y (85%)
        content_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.85))

        # View care ocupă 85% din axa x
        view = RestaurantView(size_hint_x=0.85)
        content_layout.add_widget(view)

        # Scrollbar care ocupă restul spațiului pe axa x (15%)
        scrollbar = SidebarView(size_hint_x=0.15)

        content_layout.add_widget(scrollbar)
        main_layout.add_widget(navbar)
        main_layout.add_widget(content_layout)

        self.add_widget(main_layout)
