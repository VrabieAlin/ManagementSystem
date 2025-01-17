from PySide6.QtCore import QPoint, Qt
from PySide6.QtWidgets import QScrollArea
from PySide6.QtWidgets import QScrollArea


class CustomScrollArea(QScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent)
        #self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        #self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)
        self.setMouseTracking(True)
        self.last_mouse_position = QPoint()

    def mousePressEvent(self, event):
        self.last_mouse_position = event.pos()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            delta = event.pos() - self.last_mouse_position
            self.last_mouse_position = event.pos()
            self.horizontalScrollBar().setValue(self.horizontalScrollBar().value() - delta.x())
            self.verticalScrollBar().setValue(self.verticalScrollBar().value() - delta.y())
        super().mouseMoveEvent(event)