from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QWidget, QVBoxLayout

from app.state.navbar_state import NavbarState
from app.utils.constants import Colors
from app.utils.css_utils import CSSUtils
from app.utils.widgets.labels.custom_lable_1 import CustomLabel1

ROW_NUMBER = 2
class ImageLabelWidget(QWidget):
    def __init__(self, image_path, label_text, parent=None):
        super().__init__(parent)
        self.setObjectName("ImageLabelWidget")
        self.image_label = None
        self.label_text = label_text
        self.navbar_state : NavbarState = NavbarState.instance()
        self.init_ui(image_path, label_text)
        self.setCursor(Qt.PointingHandCursor)

    def init_ui(self, image_path, label_text):
        global ROW_NUMBER
        layout = QVBoxLayout(self)
        layout.setSpacing(0)

        # Create and set up the image label
        self.image_label = QLabel()
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)

        self.image_label.setFixedSize(120, 120)  # Adjust the size as needed

        # Create and set up the text label
        text_label = CustomLabel1(label_text, self)
        text_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        #text_label.setFixedHeight(50)  # Adjust the height as needed

        # Add widgets to the layout
        layout.addWidget(self.image_label)
        layout.addWidget(text_label)


        self.setLayout(layout)

    def apply_active(self):
        self.image_label.setStyleSheet(CSSUtils.applyBackgroundColor(Colors.LIGHT_GRAY))

    def apply_inactive(self):
        self.image_label.setStyleSheet(CSSUtils.applyBackgroundColor(""))

    def mousePressEvent(self,event):
        self.navbar_state.change_view(self.label_text)
