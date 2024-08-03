from PySide6.QtCore import QMimeData, QByteArray
from PySide6.QtGui import Qt, QDrag, QPixmap, QPainter, QIcon, QMouseEvent
from PySide6.QtWidgets import QPushButton, QSizePolicy


class DraggableObject(QPushButton):
    def __init__(self, image_path, dragged_object_info=None, always_visible=False):
        super().__init__()
        self.size()
        self.setCursor(Qt.OpenHandCursor)
        self.always_visible = always_visible
        self.image = image_path
        self.dragged_object_info = dragged_object_info
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(120, 120)
        self.setIcon(QIcon(self.image))
        self.setIconSize(self.size())
        self.setStyleSheet("border: none;")
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setCursor(Qt.ClosedHandCursor)
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.setCursor(Qt.OpenHandCursor)
        super().mouseReleaseEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent):
        if event.buttons() != Qt.LeftButton:
            return

        # Pass custom data for drop event in location_editor_board
        self.dragged_object_info.image = self.image

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