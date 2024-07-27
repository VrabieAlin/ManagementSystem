from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QGridLayout, QHBoxLayout, QVBoxLayout, QFrame

from app.db.location_room_objects import LocationRoomObject
from app.screens.home_page.view.navbar_view import NavbarView
from app.screens.location_view_editor.views.draggable_object import DraggableObject
from app.screens.location_view_editor.views.location_editor_board import LocationEditorBoard
from app.utils.widgets.custom_scroll_area import CustomScrollArea


class LocationViewEditorScreen(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.db_location_room_object = LocationRoomObject(self.main_window.db_manager)
        self.setLayout(self.load_view())

    def load_view(self):
        grid_layout = QGridLayout()
        grid_layout.setContentsMargins(0, 0, 0, 0)
        grid_layout.setHorizontalSpacing(0)
        grid_layout.setVerticalSpacing(0)

        objects_layout = QHBoxLayout()
        objects_layout.setContentsMargins(0, 0, 0, 0)
        objects_layout.setSpacing(0)

        button_background_widget = QWidget()
        hbox_layout = QVBoxLayout(button_background_widget)
        hbox_layout.setContentsMargins(0, 0, 0, 0)
        hbox_layout.setSpacing(20)

        objects = self.get_objects_from_db()
        for _ in objects:
            button = DraggableObject("static/location_navbar_icon_without_bg.png", True)
            hbox_layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignHCenter)

        hbox_layout.addStretch(1)

        scroll_area = CustomScrollArea()
        scroll_area.setFixedHeight(200)
        scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        scroll_area.setWidget(button_background_widget)

        navbar = NavbarView(self.main_window)
        side_bar = scroll_area
        editor_view = LocationEditorBoard()

        grid_layout.addWidget(navbar, 0, 0, 1, 2)
        grid_layout.addWidget(editor_view, 1, 0)
        grid_layout.addWidget(side_bar, 1, 1)

        grid_layout.setColumnStretch(0, 5)
        grid_layout.setColumnStretch(1, 1)

        grid_layout.setRowStretch(0, 1)
        grid_layout.setRowStretch(1, 6)

        grid_layout.setRowMinimumHeight(0, 150)
        grid_layout.setColumnMinimumWidth(1, 100)

        return grid_layout

    def resizeEvent(self, event):
        super().resizeEvent(event)

    def get_objects_from_db(self):
        return self.db_location_room_object.load_default_objects()