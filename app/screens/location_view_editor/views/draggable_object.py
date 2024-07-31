from PySide6.QtCore import QMimeData, QByteArray, QSize
from PySide6.QtGui import Qt, QDrag, QPixmap, QPainter, QIcon
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QSizePolicy, QApplication
from PySide6.QtGui import QMouseEvent, QDragEnterEvent, QDropEvent, QPixmap

from app.utils.constants import LocationEditorConstants


class DraggableObject(QWidget):
    def __init__(self, image_path, always_visible=False,
                 canvas_size=QSize(LocationEditorConstants.CANVAS_WIDTH,LocationEditorConstants.CANVAS_HEIGHT)):
        super().__init__()
        self.setAcceptDrops(True)  # Acceptă operațiuni de drop

        self.size()
        self.setCursor(Qt.CursorShape.OpenHandCursor)
        self.always_visible = always_visible
        self.init_ui(image_path,canvas_size)

    def init_ui(self, image, canvas_size):
        # if self.always_visible: # if it's the draggable object from sidebar
        #     self.setFixedSize(120, 120)
        # else: # object created at the canvas, must be scalled with canvas dimensions
        #     # Calculate the scaling factor
        #     scale_width = canvas_size.width() / LocationEditorConstants.CANVAS_WIDTH
        #     scale_height = canvas_size.height() / LocationEditorConstants.CANVAS_HEIGHT
        #
        #     # Use the minimum scaling factor to maintain aspect ratio
        #     scale_factor = min(scale_width, scale_height)
        #
        #     # Calculate new widget size
        #     new_widget_width = int(120 * scale_factor)
        #     new_widget_height = int(120 * scale_factor)
        #
        #     self.setFixedSize(new_widget_width, new_widget_height)
        self.setFixedSize(100, 100)
        #self.setIcon(QIcon(image))
        #self.setIconSize(self.size())
        self.setStyleSheet("background-color: green;")
        self.drag_start_position = None
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event: QMouseEvent):
        if not self.drag_start_position:
            return

        if (event.pos() - self.drag_start_position).manhattanLength() < QApplication.startDragDistance():
            return

        mime_data = QMimeData()
        hot_spot = event.pos()
        data = f"{self.width()},{self.height()},{hot_spot.x()},{hot_spot.y()}".encode('utf-8')
        mime_data.setData('application/x-dnditemdata', QByteArray(data))

        # Inițializați operația de drag
        drag = QDrag(self)
        drag.setMimeData(mime_data)

        # Setarea unui pixmap pentru a vizualiza obiectul pe care îl drag
        pixmap = QPixmap(self.size())
        self.render(pixmap)
        drag.setPixmap(pixmap)

        # Începe operația de drag
        drag.exec_(Qt.MoveAction)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.source() == self and event.mimeData().hasFormat('application/x-dnditemdata'):
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event: QDropEvent):
        if event.source() == self and event.mimeData().hasFormat('application/x-dnditemdata'):
            self.move(self.mapToParent(event.pos() - self.drag_start_position))
            event.acceptProposedAction()
        else:
            event.ignore()
