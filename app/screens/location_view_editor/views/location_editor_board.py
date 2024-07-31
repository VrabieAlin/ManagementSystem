from PySide6.QtCore import Qt, QPoint, QPointF, QSizeF, QRectF
from PySide6.QtCore import Qt, QPoint, QPointF, QSize
from PySide6.QtGui import QPainter, QPen, QColor
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsProxyWidget, QGraphicsLineItem

from app.screens.location_view_editor.views.draggable_object import DraggableObject
from app.utils.constants import LocationEditorConstants


class LocationEditorBoard(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.board_objects = []
        self.setScene(QGraphicsScene(self))
        self.setAcceptDrops(True)
        self.setRenderHint(QPainter.Antialiasing)
        self.scene().setSceneRect(0, 0, LocationEditorConstants.CANVAS_WIDTH, LocationEditorConstants.CANVAS_HEIGHT)

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

            new_object = DraggableObject("static/location_navbar_icon_without_bg.png", always_visible=False,
                                         canvas_size=self.size())
            proxy_widget = self.scene().addWidget(new_object)
            self.board_objects.append(new_object)
            proxy_widget.setPos(new_pos)

            event.setDropAction(Qt.MoveAction)
            event.accept()
        else:
            event.ignore()