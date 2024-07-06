from kivy.app import App
from kivy.config import Config

from app.screen_manager.screen_manager import ScreenManager
from app.utils.constants import ScreenNames
from app.screens.home_page.home_page_screen import HomePageScreen


class MyApp(App):
    def build(self):
        # Setăm configurația pentru a porni în modul full screen
        Config.set('graphics', 'fullscreen', 'auto')

        sm = ScreenManager()
        sm.add_widget(HomePageScreen(name=ScreenNames.HOME_PAGE))
        return sm


if __name__ == "__main__":
    MyApp().run()
