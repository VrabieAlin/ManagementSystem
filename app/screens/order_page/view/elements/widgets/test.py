from PySide6.QtWidgets import QWidget, QVBoxLayout, QSpinBox, QLabel


class Test(QWidget):
    def __init__(self, parent=None):
        super().__init__()

        # Layout și elemente interne
        layout = QVBoxLayout(self)
        self.label = QLabel("Label in SpinWidget")
        self.spinbox = QSpinBox()

        layout.addWidget(self.label)
        layout.addWidget(self.spinbox)

        self.setLayout(layout)