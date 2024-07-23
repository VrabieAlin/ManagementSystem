from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QApplication

from app.utils.constants import Colors, BorderType, Texts, InputType, ScreenNames
from app.utils.css_utils import CSSUtils
from app.utils.widgets.input_modal import InputModal
from app.utils.widgets.Labels.custom_lable_1 import CustomLabel1
from app.utils.widgets.menu_modal import MenuModal
from app.utils.widgets.modal import Modal
from app.utils.widgets.widgets_utils import WidgetUtils
from app.state.state_manager import StateManager


class SidebarView(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.state_manager = StateManager.instance()
        self.setLayout(self.load_view())
        # self.apply_css()
        self.apply_view_logic()

    def load_view(self):
        # Create QVBoxLayout to place elements vertically
        self.vbox_layout = QVBoxLayout()
        self.vbox_layout.setContentsMargins(0, 0, 0, 0)
        self.vbox_layout.setSpacing(20)

        # Init elements
        name = self.state_manager.user_name
        self.name_label = CustomLabel1("" if name is None else name)
        self.login_btn = WidgetUtils.createVExpandableButton(Texts.LOGIN)
        self.logout_btn = WidgetUtils.createVExpandableButton(Texts.LOGOUT)
        self.menu_btn = WidgetUtils.createVExpandableButton(Texts.MENU)
        self.exit_btn = WidgetUtils.createVExpandableButton(Texts.EXIT)




        self.vbox_layout.addStretch(1)
        self.vbox_layout.addWidget(self.name_label, alignment=Qt.AlignHCenter)
        self.vbox_layout.addWidget(self.logout_btn, alignment=Qt.AlignHCenter)

        self.vbox_layout.addStretch(4)
        self.vbox_layout.addWidget(self.login_btn, alignment=Qt.AlignHCenter)
        self.vbox_layout.addWidget(self.menu_btn, alignment=Qt.AlignHCenter)
        self.vbox_layout.addWidget(self.exit_btn, alignment=Qt.AlignHCenter)
        self.vbox_layout.addSpacing(10)

        if self.state_manager.user_name is None:
            self.logout_btn.hide()
            self.name_label.hide()

        return self.vbox_layout

    def apply_css(self):
        # Aplică stil CSS pentru a adăuga o bordură
        self.setStyleSheet(
            CSSUtils.applyBackgroundColor(Colors.RED) +
            CSSUtils.applyBorder(2, BorderType.SOLID, Colors.BLUE)
        )

    def apply_view_logic(self):
        self.exit_btn.clicked.connect(self.show_exit_app_modal)
        self.menu_btn.clicked.connect(self.show_menu_modal)
        self.logout_btn.clicked.connect(self.logout)
        self.login_btn.clicked.connect(self.login)
        self.state_manager.state_changed.connect(self.update_ui)

    def show_menu_modal(self):
        # Complete these with const text class when options will be detailed
        menu_modal = MenuModal([Texts.LOCATION_EDITOR, "teste1", "teste2", "teste3", "teste4", "teste5", "teste6",
                                "teste7", "teste8"])
        menu_modal.menu_button.connect(self.on_modal_menu_selected)
        menu_modal.exec()

    def show_exit_app_modal(self):
        exit_dialog = Modal(Texts.MODAL_EXIT, Texts.YES, Texts.NO)
        exit_dialog.accepted.connect(self.accept_exit_app_modal)
        exit_dialog.rejected.connect(self.reject_exit_app_modal)
        exit_dialog.exec()

    def accept_exit_app_modal(self):
        QApplication.instance().quit()

    def reject_exit_app_modal(self):
        pass

    def on_modal_menu_selected(self, text):
        if text == Texts.LOCATION_EDITOR:
            self.main_window.set_screen(ScreenNames.LOCATION_VIEW_EDITOR_PAGE)

    def logout(self):
        self.state_manager.logout()

    def login(self):
        input_dialog = InputModal(Texts.LOGIN_MODAL, Texts.PASSWORD, InputType.PASSWORD, Texts.LOGIN)
        input_dialog.input_modal.connect(self.on_password_provided)
        input_dialog.exec()

    def on_password_provided(self):
        self.state_manager.login("teste")

    def update_ui(self):
        if self.state_manager.user_name is not None:
            self.name_label.setText(self.state_manager.user_name)
            self.logout_btn.show()
            self.name_label.show()
        else:
            self.logout_btn.hide()
            self.name_label.hide()
        # if self.state_manager.user_name is not None:
        #     self.vbox_layout.insertWidget(2, self.logout_btn)
        #     self.name_label.setText(self.state_manager.user_name)
        #     self.vbox_layout.insertWidget(0, self.name_label)
        # else:
        #     self.vbox_layout.removeWidget(self.logout_btn)
        #     self.vbox_layout.removeWidget(self.name_label)
