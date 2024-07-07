
from app.utils.constants import ScreenNames
from app.screens.home_page.home_page_screen import HomePageScreen
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.screens = {}
        self.screen_manager = QStackedWidget()

        #Home Screen
        self.home_screen = HomePageScreen(self)
        self.screen_manager.addWidget(self.home_screen)
        self.screens[ScreenNames.HOME_PAGE] = self.screen_manager.indexOf(self.home_screen)

        self.setCentralWidget(self.screen_manager)

        # Set fullscreen mode
        self.showFullScreen()

    def set_screen(self, screen_name):
        if screen_name in self.screens:
            self.screen_manager.setCurrentIndex(self.screens[screen_name])
        else:
            print(f"Screen {screen_name} does not exist")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MyApp()
    main_window.show()
    sys.exit(app.exec())
