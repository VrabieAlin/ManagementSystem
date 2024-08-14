from PySide6.QtCore import Qt, QPropertyAnimation, QTimer
from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton, QSizePolicy, QGraphicsOpacityEffect

from app.utils.constants import Colors


class SelectedProductMenu(QWidget):

    def __init__(self, product, close_callback, parent=None):
        super().__init__(parent)

        self.commands = {
            "edit_description":
                {
                    "name": "Editeaza descrierea",
                    "function": self.edit_description_callback,
                    "function_args": []
                },
            "modify_number":
                {
                    "name": "Modifica cantitatea",
                    "function": self.modify_number_callback,
                    "function_args": []
                },
            "void":
                {
                    "name": "Sterge produsul",
                    "function": self.void_callback,
                    "function_args": []
                },
            "void_total":
                {
                    "name": "Sterge toate produsele",
                    "function": self.void_total_callback,
                    "function_args": []
                },
            "close":
                {
                    "name": "Inchide fereastra",
                    "function": self.close_callback,
                    "function_args": []
                },
        }
        self.widgets = []
        self.product = product
        self.close_callback = close_callback

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Popup)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)

        #self.setFixedSize(300, 300)
        self.layout = QGridLayout()
        self.layout.setContentsMargins(1, 0, 0, 0)
        self.layout.setSpacing(3)

        self.setLayout(self.layout)

        self.setup_menu()


    def setup_menu(self):
        product_name_label = QLabel(self.product.name)
        #self.layout.addWidget(product_name_label, 0, 0, 1, 2)

        row = 1
        for index, command in enumerate(self.commands.values()):
            button = QPushButton(command["name"])
            button.setStyleSheet(f"""
                                QPushButton {{ 
                                    background-color: {Colors.SOFT_BLUE_2};
                                    color: {Colors.SOFT_BLUE};
                                    border: 1 solid {Colors.SOFT_BLUE};
                                    border-radius: 5px;
                                    font-size: 20px;
                                  }}""")
            if index == 0:
                button.setProperty("border-top-left-radius", "5px")
                button.setProperty("border-top-right-radius", "5px")
            elif index == len(self.commands) - 1:
                button.setProperty("border-bottom-left-radius", "5px")
                button.setProperty("border-bottom-right-radius", "5px")

            button.clicked.connect(command["function"])
            button.setFixedSize(300, 60)
            button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
            self.layout.addWidget(button, row, 0)
            self.widgets.append(button)
            row += 1


    def close_callback(self):
        self.close()

    def void_callback(self):
        pass

    def void_total_callback(self):
        # Modal de confirmare.
        pass

    def edit_description_callback(self):
        # Modal de editare descriere
        pass

    def modify_number_callback(self):
        # Modal de modificare cantitate / acelasi ca la spin_widget
        pass

    # override
    def closeEvent(self, event):
        if self.close_callback:
            self.close_callback()
        super().closeEvent(event)