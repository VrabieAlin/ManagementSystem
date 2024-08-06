from copy import deepcopy

from PySide6.QtCore import Qt, QPointF
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QGraphicsView, QGraphicsScene

from app.db.room_objects import RoomObjects
from app.state.location_editor_drag_state import LocationEditorDragState
from app.utils.constants import LocationEditorConstants
from app.utils.widgets.buttons.draggable_object import DraggableObject


class LocationEditorBoard(QGraphicsView):
    def __init__(self, main_window,parent=None):
        super().__init__(parent)
        self.setScene(QGraphicsScene(self))
        self.setAcceptDrops(True)
        self.setRenderHint(QPainter.Antialiasing)
        self.scene().setSceneRect(0, 0, LocationEditorConstants.CANVAS_WIDTH, LocationEditorConstants.CANVAS_HEIGHT)
        self.setFixedSize(LocationEditorConstants.CANVAS_WIDTH, LocationEditorConstants.CANVAS_HEIGHT)
        # Remove scroll bars
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.location_editor_drag_state: LocationEditorDragState = LocationEditorDragState.instance()
        self.db_room_objects = RoomObjects(main_window.db_manager)
        self.editor_placed_objects = self.db_room_objects.get_objects_for_room(1)
        self.load_object_on_board()

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

            dragged_item = deepcopy(self.location_editor_drag_state.context.dragged_item)
            dragged_item.x = new_pos.x()
            dragged_item.y = new_pos.y()
            self.add_object(dragged_item)
            new_object = DraggableObject(dragged_item.image, id=dragged_item.id, always_visible=False)
            proxy_widget = self.scene().addWidget(new_object)
            proxy_widget.setPos(new_pos)

            event.setDropAction(Qt.MoveAction)
            event.accept()
        else:
            event.ignore()

    def load_object_on_board(self):
        for o in self.editor_placed_objects:
            new_object = DraggableObject(o.image, id=o.id, always_visible=False)
            proxy_widget = self.scene().addWidget(new_object)
            proxy_widget.setPos(o.x,o.y)

    def add_object(self, item):
        for index, o in enumerate(self.editor_placed_objects):
            if o.id == item.id:
                self.editor_placed_objects[index] = item
                return
        self.editor_placed_objects.append(item)
