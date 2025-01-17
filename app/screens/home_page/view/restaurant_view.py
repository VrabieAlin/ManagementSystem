from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel


class RestaurantView(QWidget):
    def __init__(self, main_window):
        super(RestaurantView, self).__init__()
        self.main_window = main_window

        # Creează un QVBoxLayout
        vbox_layout = QVBoxLayout()
        vbox_layout.setContentsMargins(0, 0, 0, 0)
        vbox_layout.setSpacing(0)

        # Adaugă widget-uri la QVBoxLayout
        label1 = QLabel('')
        vbox_layout.addWidget(label1)

        # Setează layout-ul pentru widget-ul personalizat
        self.setLayout(vbox_layout)

        # Aplică stil CSS pentru a adăuga o bordură
        #self.setStyleSheet("background-color: green; border: 2px solid blue;")