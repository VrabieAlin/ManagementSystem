from PySide6.QtCore import Qt
from PySide6.QtWidgets import QScrollArea, QFrame, QWidget, QVBoxLayout, QHBoxLayout, QPushButton

from app.db.location_room_objects import LocationRoomObject
from app.utils.constants import Texts
from app.utils.widgets.buttons.draggable_object import DraggableObject
from app.utils.widgets.buttons.main_button import PrimaryButton


class SidebarEditorObjects(QScrollArea):

    def __init__(self,main_window,dragged_object_info):
        super().__init__()
        self.main_window = main_window
        self.dragged_object_info = dragged_object_info
        self.db_location_room_object = LocationRoomObject(self.main_window.db_manager)
        self.init_ui()

    def init_ui(self):
        # Main container widget
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Scroll area for draggable objects
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFrameShape(QFrame.Shape.NoFrame)

        # Container for the scroll area content
        scroll_content_widget = QWidget()
        scroll_content_layout = QVBoxLayout(scroll_content_widget)
        scroll_content_layout.setContentsMargins(0, 0, 0, 0)
        scroll_content_layout.setSpacing(20)

        objects = self.get_objects_from_db()
        for o in objects:
            button = DraggableObject(f"static/location_editor_items/{o.image}", dragged_object_info=self.dragged_object_info, always_visible=True)
            button_widget = QWidget()
            button_layout = QHBoxLayout()
            button_layout.addWidget(button, alignment=Qt.AlignCenter)
            button_widget.setLayout(button_layout)
            scroll_content_layout.addWidget(button_widget)

        scroll_content_layout.addStretch(1)  # Add stretch to push items up
        scroll_area.setWidget(scroll_content_widget)

        # Add scroll area to the main layout
        main_layout.addWidget(scroll_area)

        # Create and add the new button
        new_button = PrimaryButton(Texts.SAVE)
        main_layout.addWidget(new_button, alignment=Qt.AlignBottom)

        # Add a bottom margin for the button
        bottom_margin = QWidget()
        bottom_margin.setFixedHeight(30)  # Adjust the height for your margin
        main_layout.addWidget(bottom_margin)

        # Set the main widget as the central widget of the QScrollArea
        self.setWidget(main_widget)
        self.setWidgetResizable(True)
        self.setFrameShape(QFrame.Shape.NoFrame)

    def get_objects_from_db(self):
        return self.db_location_room_object.load_default_objects()