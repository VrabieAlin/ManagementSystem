from PySide6.QtWidgets import QPushButton, QSizePolicy, QLineEdit, QVBoxLayout, QLabel, QSpinBox

from app.utils.constants import InputType
from PySide6.QtWidgets import QPushButton, QSizePolicy
from app.utils.widgets.buttons.main_button import PrimaryButton


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

    @classmethod
    def createHExpandableInput(cls, text, placeholder, input_type):
        #TODO: refactor into a single method that receive if this
        # must be a pass input or not
        if input_type == InputType.TEXT:
            layout = QVBoxLayout()
            text_input = QLineEdit()
            text_input.setPlaceholderText(placeholder)
            text_input.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
            layout.addWidget(QLabel(text))
            layout.addWidget(text_input)
        elif input_type == InputType.PASSWORD:
            layout = QVBoxLayout()
            text_input = QLineEdit()
            text_input.setPlaceholderText(placeholder)
            text_input.setEchoMode(QLineEdit.EchoMode.Password)
            text_input.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
            layout.addWidget(QLabel(text))
            layout.addWidget(text_input)
        return layout
