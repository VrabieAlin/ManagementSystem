
from PySide6.QtWidgets import QWidget, QVBoxLayout

class ProductsMenuView(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.load_view()

    def load_view(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        item = QWidget()

        main_layout.addWidget(item)
        self.setStyleSheet("background-color: green; border: 2px solid blue;")
        self.setLayout(main_layout)