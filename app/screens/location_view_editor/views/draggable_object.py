from PySide6.QtCore import QMimeData, QByteArray
from PySide6.QtGui import Qt, QDrag, QPixmap, QPainter
from PySide6.QtWidgets import QPushButton


class DraggableObject(QPushButton):
    def __init__(self, title, always_visible=False):
        super().__init__(title)
        self.setFixedSize(100, 50)
        self.setStyleSheet("background-color: blue; color: white;")
        self.setCursor(Qt.OpenHandCursor)
        self.always_visible = always_visible

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setCursor(Qt.ClosedHandCursor)
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.setCursor(Qt.OpenHandCursor)
        super().mouseReleaseEvent(event)

    def mouseMoveEvent(self, event):
        if event.buttons() != Qt.LeftButton:
            return

        mime_data = QMimeData()
        hot_spot = event.pos() - self.rect().topLeft()
        data = f"{self.width()},{self.height()},{hot_spot.x()},{hot_spot.y()}".encode('utf-8')
        mime_data.setData('application/x-dnditemdata', QByteArray(data))

        drag = QDrag(self)
        drag.setMimeData(mime_data)

        # Create the drag pixmap
        pixmap = QPixmap(self.size())
        self.render(pixmap)

        # Create a semi-transparent pixmap for the drag operation
        shaded_pixmap = QPixmap(pixmap.size())
        shaded_pixmap.fill(Qt.transparent)

        painter = QPainter(shaded_pixmap)
        painter.setOpacity(0.5)
        painter.drawPixmap(0, 0, pixmap)
        painter.end()

        drag.setPixmap(shaded_pixmap)
        drag.setHotSpot(event.pos() - self.rect().topLeft())

        drag.exec_(Qt.MoveAction)

        # Hide the original button if it's not always visible
        if not self.always_visible:
            self.hide()