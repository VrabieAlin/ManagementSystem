import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QBoxLayout


class SidebarView(QWidget):
    def __init__(self, parent=None):
        super(SidebarView, self).__init__(parent)

        # Creează un QVBoxLayout
        vbox_layout = QVBoxLayout()

        # Adaugă widget-uri la QVBoxLayout
        label1 = QLabel('')
        vbox_layout.addWidget(label1)

        # Setează layout-ul pentru widget-ul personalizat
        self.setLayout(vbox_layout)

        # Aplică stil CSS pentru a adăuga o bordură
        self.setStyleSheet("background-color: red; border: 2px solid blue;")