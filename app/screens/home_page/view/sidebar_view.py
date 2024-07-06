from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

from app.utils.widget_utils import WidgetUtils


class SidebarView(BoxLayout):

    def __init__(self, **kwargs):
        super(SidebarView, self).__init__(**kwargs)
        WidgetUtils.SetBG(self, bg_color=[0.2, 0.6, 0.8, 1])

    def load_elements(self):
        label = Label(text="Dezen20")
        self.add_widget(label)
        login_button = Button(text="Login")
        self.add_widget(login_button)
        logout_button = Button(text="Logout")
        self.add_widget(logout_button)
        menu_button = Button(text="Menu button")
        self.add_widget(menu_button)
        exit_button = Button(text="Exit")
        self.add_widget(exit_button)
