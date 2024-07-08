import sys
from PySide6.QtWidgets import QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QScrollArea, QPushButton, QBoxLayout
from app.utils.widgets.widgets_utils import WidgetUtils
from PySide6.QtCore import Qt

from app.screens.home_page.restaurant_rooms import RoomsManager, Room, RoomObject
from app.utils.widgets.custom_scroll_area import CustomScrollArea

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
        button_background_widget.setStyleSheet("background-color: lightblue;")
        hbox_layout = QHBoxLayout(button_background_widget)


        # Creează butoane cu dimensiuni specifice
        for room in self.restaurant_rooms:
            button = WidgetUtils.createVExpandableButton(room.name)
            button.setMinimumWidth(200)
            button.setMaximumWidth(300)
            hbox_layout.addWidget(button)

        # Adaugă spatiere la QHBoxLayout dupa butoane pentru a le muta la stanga
        hbox_layout.addStretch(1)

        # Creează un QScrollArea și setează scroll_content ca widget conținut
        scroll_area = CustomScrollArea()
        scroll_area.setWidget(button_background_widget)

        # Adaugă QWidget-ul cu butoane în layout-ul principal
        main_layout.addWidget(scroll_area)

        # Setează layout-ul pentru fereastra principală
        self.setLayout(main_layout)

        # Aplică stil CSS pentru a adăuga o bordură
        self.setStyleSheet("background-color: lightblue; border: 2px solid blue;")
