from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel, QSizePolicy, QGridLayout
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QIcon, QPixmap
from datetime import datetime

from app.state.user_state import UserState
from app.utils.constants import Colors


class TopBarView(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.user_state: UserState = UserState.instance()
        self.setStyleSheet(f"color: {Colors.SOFT_BLUE}; padding-left: 10px; padding-right: 10px;")
        self.setFixedHeight(24)

        self.init_ui()

    def init_ui(self):
        self.main_layout = QGridLayout()
        self.main_layout.setContentsMargins(2, 2, 2, 2)
        self.main_layout.setSpacing(0)

        self.init_user_label()
        self.init_datetime_label()
        self.init_server_icon()
        self.position_elements()

        self.setLayout(self.main_layout)
        self.update_datetime()

        # Timer to update the date and time every second
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_datetime)
        self.timer.start(1000)

    def init_user_label(self):
        self.user_label = QLabel(f"User: {self.user_state.context['user_name']}")
        self.user_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

    def init_datetime_label(self):
        self.datetime_label = QLabel()
        self.datetime_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def init_server_icon(self):
        self.server_icon_container = QWidget()
        self.server_icon_layout = QGridLayout(self.server_icon_container)
        self.server_icon_layout.setContentsMargins(0, 0, 0, 0)
        self.server_icon_layout.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.server_icon_label = QLabel()
        pixmap = QPixmap("static/icons/connection/connection3_on.png")
        scaled_pixmap = pixmap.scaled(20, 20, Qt.AspectRatioMode.KeepAspectRatio,
                                      Qt.TransformationMode.SmoothTransformation)
        self.server_icon_label.setPixmap(scaled_pixmap)

        self.server_icon_layout.addWidget(self.server_icon_label, 0, 0)

    def position_elements(self):
        self.main_layout.addWidget(self.user_label, 0, 0)
        self.main_layout.addWidget(self.datetime_label, 0, 1)
        self.main_layout.addWidget(self.server_icon_container, 0, 2)

        self.main_layout.setColumnStretch(0, 1)
        self.main_layout.setColumnStretch(1, 1)
        self.main_layout.setColumnStretch(2, 1)

    def update_datetime(self):
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.datetime_label.setText(current_datetime)