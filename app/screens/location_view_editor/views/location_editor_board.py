from PySide6.QtCore import Qt, QRectF
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene

from app.screens.location_view_editor.views.dragable_item import DraggableItem


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
            x, y, width, height = map(int, data.split(','))
            new_item = DraggableItem(QRectF(0, 0, width, height))
            new_item.setPos(self.mapToScene(event.pos()))
            self.scene().addItem(new_item)
            event.setDropAction(Qt.MoveAction)
            event.accept()
        else:
            event.ignore()