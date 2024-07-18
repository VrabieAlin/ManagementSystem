from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QFrame
from PySide6.QtCore import Qt

from app.db.location_rooms import LocationRoom
from app.utils.widgets.custom_scroll_area import CustomScrollArea
from app.utils.widgets.Buttons.image_button import ImageLabelWidget


class NavbarView(QWidget):
    def __init__(self, main_window):
        super(NavbarView, self).__init__()
        self.main_window = main_window
        self.db_location_room = LocationRoom(self.main_window.db_manager)

        self.load_view()

    def load_view(self):
        # Creează layout-ul principal pe verticală
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Creează un QWidget pentru a acționa ca fundal pentru butoane
        button_background_widget = QWidget()
        # button_background_widget.setStyleSheet(f"background-color: {Colors.LIGHT_GRAY};")
        hbox_layout = QHBoxLayout(button_background_widget)
        hbox_layout.setContentsMargins(0, 0, 0, 0)
        hbox_layout.setSpacing(20)

        restaurant_rooms = self.get_rooms_from_db()
        # Creează butoane cu dimensiuni specifice
        for room in restaurant_rooms:
            button = ImageLabelWidget("static/location_navbar_icon_without_bg.png", room.name)
            # button.setMinimumWidth(200)
            # button.setMaximumWidth(300)
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

    def get_rooms_from_db(self):
        return self.db_location_room.load_rooms()
