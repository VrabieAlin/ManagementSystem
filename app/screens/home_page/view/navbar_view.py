import sys
from PySide6.QtWidgets import QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QScrollArea, QPushButton, QBoxLayout, \
    QFrame
from app.utils.widgets.widgets_utils import WidgetUtils
from PySide6.QtCore import Qt

from app.screens.home_page.restaurant_rooms import RoomsManager, Room, RoomObject
from app.utils.widgets.custom_scroll_area import CustomScrollArea
from app.screens.home_page.view.elements.navbar_item import ImageLabelWidget
from app.utils.constants import Colors

class NavbarView(QWidget):
    def __init__(self, main_window, **kwargs):
        super(NavbarView, self).__init__()
        self.main_window = main_window

        if 'rooms_manager' in kwargs:
            self.rooms_manager: RoomsManager = kwargs['rooms_manager']
            self.restaurant_rooms = self.rooms_manager.rooms
        else:
            self.restaurant_rooms = []
        self.load_view()

    def load_view(self):

        # Creează layout-ul principal pe verticală
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)


        # Creează un QWidget pentru a acționa ca fundal pentru butoane
        button_background_widget = QWidget()
        #button_background_widget.setStyleSheet(f"background-color: {Colors.LIGHT_GRAY};")
        hbox_layout = QHBoxLayout(button_background_widget)
        hbox_layout.setContentsMargins(0, 0, 0, 0)
        hbox_layout.setSpacing(20)


        # Creează butoane cu dimensiuni specifice
        for room in self.restaurant_rooms:
            button = ImageLabelWidget("static/location_navbar_icon_without_bg.png", room.name)
            #button.setMinimumWidth(200)
            #button.setMaximumWidth(300)
            hbox_layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignHCenter)

        # Adaugă spatiere la QHBoxLayout dupa butoane pentru a le muta la stanga
        hbox_layout.addStretch(1)

        # Creează un QScrollArea și setează scroll_content ca widget conținut
        scroll_area = CustomScrollArea()
        scroll_area.setFixedHeight(200)
        scroll_area.setFrameShape(QFrame.NoFrame)
        scroll_area.setWidget(button_background_widget)

        # Adaugă QWidget-ul cu butoane în layout-ul principal
        main_layout.addWidget(scroll_area)

        # Setează layout-ul pentru fereastra principală
        self.setLayout(main_layout)

