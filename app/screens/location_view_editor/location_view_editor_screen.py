from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QGridLayout, QHBoxLayout, QVBoxLayout, QFrame, QScrollArea

from app.db.location_room_objects import LocationRoomObject
from app.screens.home_page.view.navbar_view import NavbarView
from app.screens.location_view_editor.utils.dragged_object_info import DraggedObjectInfo
from app.screens.location_view_editor.views.sidebar_editor_objects import SidebarEditorObjects
from app.utils.widgets.buttons.draggable_object import DraggableObject
from app.screens.location_view_editor.views.location_editor_board import LocationEditorBoard


class LocationViewEditorScreen(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.editor_view = None
        self.main_window = main_window
        self.dragged_object_info = DraggedObjectInfo()
        self.setLayout(self.load_view())

    def load_view(self):
        grid_layout = QGridLayout()
        grid_layout.setContentsMargins(0, 0, 0, 0)
        grid_layout.setHorizontalSpacing(0)
        grid_layout.setVerticalSpacing(0)

        editor_view = LocationEditorBoard(dragged_object_info=self.dragged_object_info)
        sidebar_editor_objects = SidebarEditorObjects(self.main_window,dragged_object_info=self.dragged_object_info)

        navbar = NavbarView(self.main_window)

        grid_layout.addWidget(navbar, 0, 0, 1, 2)
        grid_layout.addWidget(editor_view, 1, 0, alignment=Qt.AlignCenter)  # Center the editor view
        grid_layout.addWidget(sidebar_editor_objects, 1, 1)

        grid_layout.setColumnStretch(0, 5)
        grid_layout.setColumnStretch(1, 1)

        grid_layout.setRowStretch(0, 1)
        grid_layout.setRowStretch(1, 6)

        grid_layout.setRowMinimumHeight(0, 150)
        grid_layout.setColumnMinimumWidth(1, 200)

        return grid_layout

    def resizeEvent(self, event):
        super().resizeEvent(event)
