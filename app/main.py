from app.screens.location_view_editor.location_view_editor_screen import LocationViewEditorScreen
from app.utils.constants import ScreenNames
from app.screens.home_page.home_page_screen import HomePageScreen
from app.screens.order_page.order_page_screen import OrderPage
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from app.db.db_manager import DBManager
from app.db.for_testing.db_populator import DBInserter

from PySide6.QtGui import QPalette, QColor

'''
Color pallete:

Alb Pur (#FFFFFF) - Pentru fundaluri și spații mari, pentru a păstra un aspect curat și aerisit.
Gri Deschis (#F5F5F5) - Pentru elemente de fundal secundare și secțiuni care necesită o ușoară diferențiere față de alb.
Gri Mediu (#CCCCCC) - Pentru delimitarea secțiunilor și contururi subtile.
Gri Închis (#333333) - Pentru textul principal și elementele de navigație, oferind un contrast puternic și claritate.
Albastru Soft (#4A90E2) - Pentru butoane și elemente de interacțiune principală, aducând un accent de culoare profesional și plăcut.
Verde Deschis (#50E3C2) - Pentru confirmări și mesaje de succes, aducând un sentiment de siguranță și pozitivitate.
Roșu Deschis (#FF6F61) - Pentru erori și alerte, atrăgând atenția fără a fi prea agresiv.
Portocaliu Deschis (#FFA500) - Pentru mesaje de avertizare și informații importante.

    
'''
class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        #init db manager
        self.db_manager = DBManager()
        self.db_insertor_for_testing = DBInserter(self.db_manager).populate_tables()

        self.screens = {}
        self.screen_manager = QStackedWidget()
        self.setContentsMargins(0, 0, 0, 0)

        #Set background collor
        p = self.palette()
        p.setColor(QPalette.Window, QColor("#DDDDDD"))

        # Apply the palette to the main window
        self.setPalette(p)



        #Home Screen
        self.home_screen = HomePageScreen(self)

        self.screen_manager.addWidget(self.home_screen)
        self.screens[ScreenNames.HOME_PAGE] = self.screen_manager.indexOf(self.home_screen)

        #Order Screen
        self.order_screen = OrderPage(self)

        self.screen_manager.addWidget(self.order_screen)
        self.screens[ScreenNames.ORDER_PAGE] = self.screen_manager.indexOf(self.order_screen)

        #Business location editor Screen
        self.location_view_editor_screen = LocationViewEditorScreen(self)

        self.screen_manager.addWidget(self.location_view_editor_screen)
        self.screens[ScreenNames.LOCATION_VIEW_EDITOR_PAGE] = self.screen_manager.indexOf(self.location_view_editor_screen)

        #Set main screen
        self.setCentralWidget(self.screen_manager)
        self.set_screen(ScreenNames.LOCATION_VIEW_EDITOR_PAGE)

        # Set fullscreen mode
        self.showFullScreen()

        #Update page
        self.order_screen.refresh_graphic()


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
