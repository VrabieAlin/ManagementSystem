from PySide6.QtWidgets import QPushButton, QSizePolicy
from app.utils.widgets.Buttons.main_button import PrimaryButton


class WidgetUtils:

    @classmethod
    def createVExpandableButton(cls, text):
        btn = PrimaryButton(text)
        btn.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        return btn

    @classmethod
    def createHExpandableButton(cls, text):
        btn = PrimaryButton(text)
        btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        return btn