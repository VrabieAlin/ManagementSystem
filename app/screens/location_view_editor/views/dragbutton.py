from PySide6.QtCore import QMimeData, QByteArray
from PySide6.QtGui import Qt, QDrag
from PySide6.QtWidgets import QPushButton


class DragButton(QPushButton):
    def __init__(self, title, parent=None):
        super().__init__(title, parent)
        self.setFixedSize(100, 50)

    def mouseMoveEvent(self, event):
        if event.buttons() != Qt.LeftButton:
            return

        mime_data = QMimeData()
        data = f"0,0,{self.width()},{self.height()}".encode('utf-8')
        mime_data.setData('application/x-dnditemdata', QByteArray(data))

        drag = QDrag(self)
        drag.setMimeData(mime_data)
        drag.setHotSpot(event.pos() - self.rect().topLeft())

        drop_action = drag.exec_(Qt.MoveAction)