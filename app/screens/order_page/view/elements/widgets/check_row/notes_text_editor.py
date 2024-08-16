from PySide6.QtWidgets import QTextEdit
from PySide6.QtGui import QFont

from app.screens.order_page.view.elements.widgets.check_row.modals.edit_description_dialog import EditDescriptionDialog


class NotesTextEditor(QTextEdit):
    def __init__(self, basket_product, update_note_callback, parent=None):
        super().__init__(parent)
        self.basket_product = basket_product
        self.update_note_callback = update_note_callback

        self.setText(self.basket_product.notes)

        # Set font for QTextEdit
        font = QFont("Arial", 16)
        self.setFont(font)

    def mousePressEvent(self, event):
        dialog = EditDescriptionDialog(self.basket_product, self.update_note_callback, self)
        if dialog.exec():
            print("Description updated:", self.basket_product.notes)
        #super().mousePressEvent(event)