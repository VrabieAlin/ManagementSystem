from PySide6.QtCore import QMimeData, QByteArray, QSize
from PySide6.QtGui import Qt, QDrag, QPixmap, QPainter, QIcon
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QSizePolicy

from app.utils.constants import LocationEditorConstants


class DraggableObject(QPushButton):
    def __init__(self, image_path, always_visible=False,
                 canvas_size=QSize(LocationEditorConstants.CANVAS_WIDTH,LocationEditorConstants.CANVAS_HEIGHT)):
        super().__init__()
        self.size()
        self.setCursor(Qt.OpenHandCursor)
        self.always_visible = always_visible
        self.init_ui(image_path,canvas_size)

    def init_ui(self, image,canvas_size):
        if self.always_visible: # if it's the draggable object from sidebar
            self.setFixedSize(120, 120)
        else: # object created at the canvas, must be scalled with canvas dimensions
            # Calculate the scaling factor
            scale_width = canvas_size.width() / LocationEditorConstants.CANVAS_WIDTH
            scale_height = canvas_size.height() / LocationEditorConstants.CANVAS_HEIGHT

            # Use the minimum scaling factor to maintain aspect ratio
            scale_factor = min(scale_width, scale_height)

            # Calculate new widget size
            new_widget_width = int(120 * scale_factor)
            new_widget_height = int(120 * scale_factor)

            self.setFixedSize(new_widget_width, new_widget_height)

        self.setIcon(QIcon(image))
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