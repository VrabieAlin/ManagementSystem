from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush
from PySide6.QtWidgets import QGraphicsRectItem


class DraggableItem(QGraphicsRectItem):
    def __init__(self, rect, parent=None):
        super().__init__(rect, parent)
        self.setBrush(QBrush(Qt.blue))
        self.setFlags(QGraphicsRectItem.ItemIsMovable | QGraphicsRectItem.ItemIsSelectable)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setCursor(Qt.ClosedHandCursor)
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.setCursor(Qt.ArrowCursor)
        super().mouseReleaseEvent(event)