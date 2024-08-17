from PySide6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QDialogButtonBox, QDialog, QGridLayout, QPushButton, \
    QSizePolicy, QLabel
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

from app.utils.constants import Colors


class EditQuantityDialog(QDialog):
    def __init__(self, basket_product, update_description_callback, parent=None):
        super().__init__(parent)
        self.char_limit = 100
        self.basket_product = basket_product
        self.update_description_callback = update_description_callback

        self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.FramelessWindowHint)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.setFixedSize(400, 600)

        self.setObjectName("edit_description_dialog")
        self.setStyleSheet(f"""
                             QLabel {{
                                background-color: {Colors.SOFT_BLUE_2};
                                color: {Colors.SOFT_BLUE};
                                border: 1 solid {Colors.SOFT_BLUE};
                                border-top-left-radius: 5px;
                                border-top-right-radius: 5px;
                                font-size: 26px;
                                font-weight: bold;
                            }}
                            QPushButton {{
                                background-color: {Colors.SOFT_BLUE};
                                color: white;
                                border: 1 solid {Colors.BLACK};
                                font-size: 26px;
                                
                            }}
                            """)

        self.load_view()
        self.center()

    def center(self):
        if self.parent():
            screen = self.parent().screen()
            screen_geometry = screen.geometry()
            dialog_geometry = self.geometry()
            x = screen_geometry.x() + (screen_geometry.width() - dialog_geometry.width()) // 2
            y = screen_geometry.y() + (screen_geometry.height() - dialog_geometry.height()) // 2
            self.move(x, y)

    def load_view(self):
        self.layout = QGridLayout(self)
        self.layout.setContentsMargins(5, 5, 5, 5)
        self.layout.setSpacing(0)

        self.init_label()
        self.init_keyboard()
        self.init_button_box()

        self.layout.setRowStretch(0, 1)
        self.layout.setRowStretch(1, 8)
        self.layout.setRowStretch(2, 1)

        self.layout.setColumnStretch(0, 1)
        self.layout.setColumnStretch(1, 1)

        self.setLayout(self.layout)

    def init_label(self):
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont("Arial", 20)
        self.label.setFont(font)
        self.layout.addWidget(self.label, 0, 0, 1, 2)

    def init_keyboard(self):
        self.buttons = {}
        button_layout = QGridLayout()

        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2),
            ('0', 3, 0), ('.', 3, 1), ('Del', 3, 2),
        ]

        for text, row, col in buttons:
            button = QPushButton(text)
            button.setMinimumHeight(60)
            font = QFont("Arial", 20)
            button.setFont(font)
            button.clicked.connect(self.on_button_clicked)
            button_layout.addWidget(button, row, col)
            self.buttons[text] = button

        self.layout.addLayout(button_layout, 1, 0, 1, 2)

    def on_button_clicked(self):
        button = self.sender()
        text = button.text()

        if text == 'Del':
            current_text = self.label.text()
            self.label.setText(current_text[:-1])
        else:
            current_text = self.label.text()
            self.label.setText(current_text + text)

    def init_button_box(self):
        ok_button = QPushButton("Save")
        cancel_button = QPushButton("Exit")

        ok_button.setMinimumHeight(60)
        cancel_button.setMinimumHeight(60)
        font = QFont("Arial", 20)
        ok_button.setFont(font)
        cancel_button.setFont(font)

        ok_button.setStyleSheet(f"""
                                QPushButton {{
                                    background-color: {Colors.LIGHT_GREEN};
                                    color: {Colors.WHITE};
                                    border-bottom-left-radius: 5px;
                                }}
                                """)

        cancel_button.setStyleSheet(f"""
                                QPushButton {{
                                    background-color: {Colors.SOFT_RED};
                                    color: {Colors.WHITE};
                                    border-bottom-right-radius: 5px;
                                }}
                                """)

        ok_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        cancel_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        ok_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)

        self.layout.addWidget(ok_button, 2, 0)
        self.layout.addWidget(cancel_button, 2, 1)

    def accept(self):
        self.update_description_callback(self.label.text())
        super().accept()