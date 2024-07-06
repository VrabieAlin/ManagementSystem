# from kivy.app import App
# from kivy.config import Config
#
from app.screen_manager.screen_manager import ScreenManager
from app.utils.constants import ScreenNames
from app.screens.home_page.home_page_screen import HomePageScreen
import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        sm = ScreenManager()

        layout = HomePageScreen().getLayout()
        #layout = QVBoxLayout()
        self.setLayout(layout)

        # Set fullscreen mode
        self.showFullScreen()


# class MyWidget(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]
#
#         self.button = QtWidgets.QPushButton("Click me!")
#         self.text = QtWidgets.QLabel("Hello World",
#                                      alignment=QtCore.Qt.AlignCenter)
#
#         self.layout = QtWidgets.QVBoxLayout(self)
#         self.layout.addWidget(self.text)
#         self.layout.addWidget(self.button)
#
#         self.button.clicked.connect(self.magic)
#
#     @QtCore.Slot()
#     def magic(self):
#         self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MyApp()
    sys.exit(app.exec())
    #MyApp().show()
