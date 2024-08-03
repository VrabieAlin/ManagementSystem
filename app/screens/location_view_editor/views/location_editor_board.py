from PySide6.QtCore import Qt, QPointF
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene

from app.utils.widgets.buttons.draggable_object import DraggableObject
from app.utils.constants import LocationEditorConstants


class LocationEditorBoard(QGraphicsView):
    def __init__(self, dragged_object_info=None, parent=None):
        super().__init__(parent)
        self.setScene(QGraphicsScene(self))
        self.setAcceptDrops(True)
        self.setRenderHint(QPainter.Antialiasing)
        self.scene().setSceneRect(0, 0, LocationEditorConstants.CANVAS_WIDTH, LocationEditorConstants.CANVAS_HEIGHT)
        self.setFixedSize(LocationEditorConstants.CANVAS_WIDTH,LocationEditorConstants.CANVAS_HEIGHT)
        # Remove scroll bars
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.dragged_object_info = dragged_object_info

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat('application/x-dnditemdata'):
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasFormat('application/x-dnditemdata'):
            event.setDropAction(Qt.MoveAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasFormat('application/x-dnditemdata'):
            byte_array = event.mimeData().data('application/x-dnditemdata')
            data = byte_array.data().decode('utf-8')
            width, height, hot_x, hot_y = map(int, data.split(','))

            drop_pos = self.mapToScene(event.pos())
            new_pos = drop_pos - QPointF(hot_x, hot_y)

            new_object = DraggableObject(self.dragged_object_info.image, dragged_object_info=self.dragged_object_info,
                                         always_visible=False)
            proxy_widget = self.scene().addWidget(new_object)
            proxy_widget.setPos(new_pos)

            event.setDropAction(Qt.MoveAction)
            event.accept()
        else:
            event.ignore()