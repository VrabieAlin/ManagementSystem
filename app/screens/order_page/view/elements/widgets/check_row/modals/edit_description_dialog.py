from PySide6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QDialogButtonBox, QDialog, QGridLayout, QPushButton, \
    QSizePolicy
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

from app.utils.constants import Colors


class EditDescriptionDialog(QDialog):
    def __init__(self, basket_product, update_description_callback, parent=None):
        super().__init__(parent)
        self.char_limit = 100
        self.basket_product = basket_product
        self.update_description_callback = update_description_callback

        self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.FramelessWindowHint)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.setFixedSize(500, 400)

        self.setObjectName("edit_description_dialog")
        self.setStyleSheet(f"""
                             QTextEdit {{ 
                                background-color: {Colors.SOFT_BLUE_2};
                                color: {Colors.SOFT_BLUE};
                                border: 1 solid {Colors.SOFT_BLUE};
                                border-top-left-radius: 5px;
                                border-top-right-radius: 5px;
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

        self.init_text_edit()
        self.init_button_box()

        self.layout.setRowStretch(0, 4)
        self.layout.setRowStretch(0, 1)

        self.layout.setColumnStretch(0, 1)
        self.layout.setColumnStretch(1, 1)

        self.setLayout(self.layout)

    def init_text_edit(self):
        self.text_edit = QTextEdit(self)
        self.text_edit.textChanged.connect(self.check_character_limit)

        self.text_edit.setText(self.basket_product.notes)
        self.text_edit.moveCursor(self.text_edit.textCursor().MoveOperation.End)

        font = QFont("Arial", 20)
        self.text_edit.setFont(font)
        self.layout.addWidget(self.text_edit, 0, 0, 1, 2)

    def init_button_box(self):
        # Crearea butoanelor OK și Cancel
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

        # Conectarea butoanelor la sloturile accept și reject
        ok_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)

        self.layout.addWidget(ok_button, 1, 0)
        self.layout.addWidget(cancel_button, 1, 1)

    def check_character_limit(self):
        # Obținem textul curent din QTextEdit
        text = self.text_edit.toPlainText()

        # Verificăm dacă numărul de caractere depășește limita
        if len(text) > self.char_limit:
            # Tăiem textul la limita dorită
            self.text_edit.blockSignals(True)  # Blocăm semnalele pentru a evita recursivitatea
            self.text_edit.setPlainText(text[:self.char_limit])
            self.text_edit.blockSignals(False)  # Deblocăm semnalele

            # Mutăm cursorul la sfârșitul textului
            self.text_edit.moveCursor(self.text_edit.textCursor().MoveOperation.End)


    def accept(self):
        self.update_description_callback(self.text_edit.toPlainText())
        super().accept()