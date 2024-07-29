from PySide6.QtCore import Qt, QPoint, QPointF, QSize
from PySide6.QtGui import QPainter, QPen, QColor
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsProxyWidget, QGraphicsLineItem

from app.screens.location_view_editor.views.draggable_object import DraggableObject


class LocationEditorBoard(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setScene(QGraphicsScene(self))
        self.setAcceptDrops(True)
        self.setRenderHint(QPainter.Antialiasing)
        self.scene().setSceneRect(0, 0, 800, 600)
        self.guidelines = []  # To store reference to guidelines
        self.item_positions = []  # To track item positions



    def draw_guidelines(self, item=None):
        # Clear existing guidelines
        for line in self.guidelines:
            self.scene().removeItem(line)
        self.guidelines.clear()

        if item is None:
            return

        # Get all items in the scene
        items = self.scene().items()
        item_rect = item.sceneBoundingRect()

        for existing_item in items:
            if isinstance(existing_item, QGraphicsProxyWidget):
                existing_rect = existing_item.sceneBoundingRect()
                x1 = existing_rect.left()
                x2 = existing_rect.right()
                y1 = existing_rect.top()
                y2 = existing_rect.bottom()

                # Vertical guides
                self.add_guide(x1, 0, x1, self.sceneRect().height())
                self.add_guide(x2, 0, x2, self.sceneRect().height())

                # Horizontal guides
                self.add_guide(0, y1, self.sceneRect().width(), y1)
                self.add_guide(0, y2, self.sceneRect().width(), y2)

    def add_guide(self, x1, y1, x2, y2):
        line = QGraphicsLineItem(x1, y1, x2, y2)
        line.setPen(QPen(QColor(255, 0, 0, 255), 1, Qt.DashLine))
        self.guidelines.append(line)
        self.scene().addItem(line)

    def mouseMoveEvent(self, event):
        super().mouseMoveEvent(event)
        if self.dragging_item:
            self.draw_guidelines(self.dragging_item)

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
            snap_pos = self.snap_to_guidelines(drop_pos)
            new_pos = snap_pos - QPointF(hot_x, hot_y)

            new_object = DraggableObject("static/location_navbar_icon_without_bg.png", always_visible=False)
            #new_object.setFixedSize(QSize(int(new_object.width() * 1.5), int(new_object.height() * 1.2)))
            proxy_widget = self.scene().addWidget(new_object)
            proxy_widget.setPos(new_pos)

            event.setDropAction(Qt.MoveAction)
            event.accept()
        else:
            event.ignore()

    def snap_to_guidelines(self, pos):
        # Adjust this method to snap to guidelines if necessary
        return pos

    def start_drag(self, item):
        self.dragging_item = item

    def end_drag(self):
        self.dragging_item = None
        self.draw_guidelines()