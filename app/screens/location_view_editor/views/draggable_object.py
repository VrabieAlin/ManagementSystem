from PySide6.QtCore import QMimeData, QByteArray
from PySide6.QtGui import Qt, QDrag, QPixmap, QPainter, QIcon
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton


class DraggableObject(QPushButton):
    def __init__(self, image_path, always_visible=False):
        super().__init__()
        self.setCursor(Qt.OpenHandCursor)
        self.always_visible = always_visible
        self.init_ui(image_path)

    def init_ui(self, image):
        self.setFixedSize(120, 120)  # Adjust the size as needed
        self.setIcon(QIcon(image))
        self.setIconSize(self.size())
        self.setStyleSheet("border: none;")  # Remove the border

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setCursor(Qt.ClosedHandCursor)
            if self.parent():
                self.parent().start_drag(self)
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.setCursor(Qt.OpenHandCursor)
        if self.parent():
            self.parent().end_drag()
        super().mouseReleaseEvent(event)


    def mouseMoveEvent(self, event):
        if event.buttons() != Qt.LeftButton:
            return

        mime_data = QMimeData()
        hot_spot = event.pos()
        data = f"{self.width()},{self.height()},{hot_spot.x()},{hot_spot.y()}".encode('utf-8')
        mime_data.setData('application/x-dnditemdata', QByteArray(data))

        drag = QDrag(self)
        drag.setMimeData(mime_data)

        pixmap = QPixmap(self.size())
        self.render(pixmap)

        shaded_pixmap = QPixmap(pixmap.size())
        shaded_pixmap.fill(Qt.transparent)

        painter = QPainter(shaded_pixmap)
        painter.setOpacity(0.5)
        painter.drawPixmap(0, 0, pixmap)
        painter.end()

        drag.setPixmap(shaded_pixmap)
        drag.setHotSpot(event.pos())

        drag.exec_(Qt.MoveAction)

        if not self.always_visible:
            self.hide()