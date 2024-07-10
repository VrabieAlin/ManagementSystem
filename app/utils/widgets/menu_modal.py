from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout

from app.utils.widgets.widgets_utils import WidgetUtils


class MenuModal(QDialog):

    def __init__(self):
        super().__init__()

        # Remove the app bar present in os applications (the one that have a title and minimize, maximize, close button)
        self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.FramelessWindowHint)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)

        btn1 = WidgetUtils.createHExpandableButton("teste")
        btn2 = WidgetUtils.createHExpandableButton("teste")
        btn3 = WidgetUtils.createHExpandableButton("teste")
        btn4 = WidgetUtils.createHExpandableButton("teste")
        btn5 = WidgetUtils.createHExpandableButton("teste")
        btn6 = WidgetUtils.createHExpandableButton("teste")
        btn7 = WidgetUtils.createHExpandableButton("teste")
        btn8 = WidgetUtils.createHExpandableButton("teste")
        btn9 = WidgetUtils.createHExpandableButton("teste")

        # Create a menu modal with buttons. As we don't know now what button we have, we'll choose a modal with
        # 3 rows and 3 buttons each row
        l1 = QHBoxLayout()
        l1.addWidget(btn1)
        l1.addWidget(btn2)
        l1.addWidget(btn3)
        l2 = QHBoxLayout()
        l2.addWidget(btn4)
        l2.addWidget(btn5)
        l2.addWidget(btn6)
        l3 = QHBoxLayout()
        l3.addWidget(btn7)
        l3.addWidget(btn8)
        l3.addWidget(btn9)

        layout_modal = QVBoxLayout()
        layout_modal.addLayout(l1)
        layout_modal.addLayout(l2)
        layout_modal.addLayout(l3)

        self.setLayout(layout_modal)
