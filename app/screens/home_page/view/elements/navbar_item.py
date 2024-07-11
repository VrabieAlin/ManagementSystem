from PySide6.QtWidgets import QLabel, QWidget, QVBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from app.utils.constants import Colors
from app.utils.widgets.Labels.custom_lable_1 import CustomLabel1

class ImageLabelWidget(QWidget):
    def __init__(self, image_path, label_text, parent=None):
        super().__init__(parent)
        self.setObjectName("ImageLabelWidget")
        self.init_ui(image_path, label_text)

    def init_ui(self, image_path, label_text):
        layout = QVBoxLayout(self)

        # Create and set up the image label
        image_label = QLabel(self)
        pixmap = QPixmap(image_path)
        image_label.setPixmap(pixmap)
        image_label.setScaledContents(True)
        image_label.setFixedSize(120, 120)  # Adjust the size as needed

        # Create and set up the text label
        text_label = CustomLabel1(label_text, self)
        #text_label.setAlignment(Qt.AlignCenter)

        #text_label.setFixedHeight(50)  # Adjust the height as needed

        # Add widgets to the layout
        layout.addWidget(image_label)
        layout.addWidget(text_label)

        self.setLayout(layout)