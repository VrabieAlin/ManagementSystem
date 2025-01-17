from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QFrame

from app.db.location_rooms import LocationRoom
from app.state.navbar_state import NavbarState
from app.utils.widgets.buttons.image_button import ImageLabelWidget
from app.utils.widgets.custom_scroll_area import CustomScrollArea


class NavbarView(QWidget):
    def __init__(self, main_window):
        super(NavbarView, self).__init__()
        self.main_window = main_window
        self.db_location_room = LocationRoom(self.main_window.db_manager)
        self.buttons = []
        self.navbar_state: NavbarState = NavbarState.instance()
        self.load_view()
        self.navbar_state.view_selected.connect(self.set_active_view)

    def load_view(self):
        # Creează layout-ul principal pe verticală
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Creează un QWidget pentru a acționa ca fundal pentru butoane
        button_background_widget = QWidget()
        hbox_layout = QHBoxLayout(button_background_widget)
        hbox_layout.setContentsMargins(0, 0, 0, 0)
        hbox_layout.setSpacing(20)

        restaurant_rooms = self.get_rooms_from_db()
        self.navbar_state.change_view(restaurant_rooms[0].id)
        # Creează butoane cu dimensiuni specifice
        for room in restaurant_rooms:
            button = ImageLabelWidget("static/location_navbar_icon_without_bg.png", room.name,room.id)
            hbox_layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignHCenter)
            self.buttons.append(button)

        # Adaugă spatiere la QHBoxLayout dupa butoane pentru a le muta la stanga
        hbox_layout.addStretch(1)

        # Creează un QScrollArea și setează scroll_content ca widget conținut
        scroll_area = CustomScrollArea()
        scroll_area.setFixedHeight(200)
        scroll_area.setFrameShape(QFrame.Shape.NoFrame)
        scroll_area.setWidget(button_background_widget)

        # Adaugă QWidget-ul cu butoane în layout-ul principal
        main_layout.addWidget(scroll_area)

        # Setează layout-ul pentru fereastra principală
        self.setLayout(main_layout)

    def get_rooms_from_db(self):
        return self.db_location_room.load_rooms()

    def set_active_view(self):
        view_selected = self.navbar_state.context.active_view
        for b in self.buttons:
            if b.id == view_selected:
                b.apply_active()
            else:
                b.apply_inactive()
