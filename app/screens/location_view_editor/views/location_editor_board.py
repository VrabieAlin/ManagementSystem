from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene

from app.screens.location_view_editor.views.draggable_object import DraggableObject


class LocationEditorBoard(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setScene(QGraphicsScene(self))
        self.setAcceptDrops(True)
        self.setRenderHint(QPainter.Antialiasing)
        self.scene().setSceneRect(0, 0, 800, 600)

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

            # Calculate the new position by adjusting for the hotspot
            drop_pos = self.mapToScene(event.pos())
            new_pos = drop_pos - QPoint(hot_x, hot_y)

            # Create a new DraggableObject at the dropped position
            new_object = DraggableObject("Dragged")
            proxy_widget = self.scene().addWidget(new_object)
            proxy_widget.setPos(new_pos)

            event.setDropAction(Qt.MoveAction)
            event.accept()
        else:
            event.ignore()