from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QDialog, QDialogButtonBox, QApplication

from app.utils.constants import Colors, BorderType, Texts
from app.utils.css_utils import CSSUtils
from app.utils.widgets.modal import Modal
from app.utils.widgets.widgets_utils import WidgetUtils


class SidebarView(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setLayout(self.loadViews())
        self.apply_css()
        self.apply_view_logic()

    def loadViews(self):
        # Create QVBoxLayout to place elements vertically
        vbox_layout = QVBoxLayout()
        vbox_layout.setContentsMargins(0, 0, 0, 0)
        vbox_layout.setSpacing(0)

        # Init elements
        self.name_label = QLabel('Dezen20')
        self.name_label.setFixedHeight(150)
        self.login_btn = WidgetUtils.createVExpandableButton(Texts.LOGIN)
        self.logout_btn = WidgetUtils.createVExpandableButton(Texts.LOGOUT)
        self.menu_btn = WidgetUtils.createVExpandableButton(Texts.MENU)
        self.exit_btn = WidgetUtils.createVExpandableButton(Texts.EXIT)

        vbox_layout.addWidget(self.name_label)
        vbox_layout.addWidget(self.login_btn)
        vbox_layout.addWidget(self.logout_btn)
        vbox_layout.addWidget(self.menu_btn)
        vbox_layout.addWidget(self.exit_btn)

        return vbox_layout

    def apply_css(self):
        # Aplică stil CSS pentru a adăuga o bordură
        self.setStyleSheet(
            CSSUtils.applyBackgroundColor(Colors.RED) +
            CSSUtils.applyBorder(2, BorderType.SOLID, Colors.BLUE)
        )

    def apply_view_logic(self):
        self.exit_btn.clicked.connect(self.show_exit_app_modal)

    def show_exit_app_modal(self):
        exit_dialog = Modal(Texts.MODAL_EXIT, Texts.YES, Texts.NO)
        exit_dialog.accepted.connect(self.accept_exit_app_modal)
        exit_dialog.rejected.connect(self.reject_exit_app_modal)
        exit_dialog.exec()

    def accept_exit_app_modal(self):
        QApplication.instance().quit()

    def reject_exit_app_modal(self):
        pass
