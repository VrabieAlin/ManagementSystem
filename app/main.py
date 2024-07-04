from kivy.config import Config
from views.home import home_main

if __name__ == "__main__":
    # Setăm configurația pentru a porni în modul full screen
    Config.set('graphics', 'fullscreen', 'auto')
    home_main.load_page()