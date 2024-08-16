from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QVBoxLayout, QTextEdit
from PySide6.QtGui import QFont, QTextCursor

from app.screens.order_page.model.basket_product import BasketProduct
from app.screens.order_page.view.elements.widgets.check_row.modals.edit_description_dialog import EditDescriptionDialog
from app.screens.order_page.view.elements.widgets.check_row.notes_text_editor import NotesTextEditor
from app.utils.constants import Colors


class NotesEditor(QDialog):
    def __init__(self, basket_product: BasketProduct, update_note_callback, close_callback, parent=None):
        super().__init__(parent)

        self.setContentsMargins(0, 0, 0, 0)
        self.update_note_callback = update_note_callback
        self.close_callback = close_callback
        self.basket_product = basket_product

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Dialog)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)

        self.load_view()

    def load_view(self):
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(5, 5, 5, 0)
        self.setStyleSheet(f"""
                                background-color: {Colors.SOFT_BLUE_2};
                                color: {Colors.SOFT_BLUE};
                                border: 1 solid {Colors.SOFT_BLUE};
                                border-radius: 5px;
                                font-size: 20px;
                              """)

        self.text_edit = NotesTextEditor(self.basket_product, self.update_note_callback, self)
        self.layout.addWidget(self.text_edit)
        self.setLayout(self.layout)

        self.setFixedSize(self.parent().width() - 10, 120)


    def closeEvent(self, event):
        if self.close_callback:
            self.close_callback()
        super().closeEvent(event)