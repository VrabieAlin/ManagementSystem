from PySide6.QtWidgets import QPushButton, QSizePolicy


class WidgetUtils:

    @classmethod
    def createVExpandableButton(cls, text):
        btn = QPushButton(text)
        btn.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        return btn

    @classmethod
    def createHExpandableButton(cls, text):
        btn = QPushButton(text)
        btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        return btn