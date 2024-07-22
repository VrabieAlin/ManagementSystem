from PySide6.QtWidgets import QWidget, QGridLayout

from app.screens.home_page.view.navbar_view import NavbarView
from app.screens.location_view_editor.views.dragbutton import DragButton
from app.screens.location_view_editor.views.location_editor_board import LocationEditorBoard


class LocationViewEditorScreen(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setLayout(self.load_view())

    def load_view(self):
        grid_layout = QGridLayout()
        grid_layout.setContentsMargins(0, 0, 0, 0)
        grid_layout.setHorizontalSpacing(0)
        grid_layout.setVerticalSpacing(0)

        # Init views
        navbar = NavbarView(self.main_window)
        side_bar = DragButton('Drag me')
        editor_view = LocationEditorBoard()

        grid_layout.addWidget(navbar, 0, 0, 1, 2)
        grid_layout.addWidget(editor_view, 1, 0)
        grid_layout.addWidget(side_bar, 1, 1)

        grid_layout.setColumnStretch(0, 5)
        grid_layout.setColumnStretch(1, 1)

        grid_layout.setRowStretch(0, 1)
        grid_layout.setRowStretch(1, 6)

        grid_layout.setRowMinimumHeight(0, 150)
        grid_layout.setColumnMinimumWidth(1, 100)

        return grid_layout

    def resizeEvent(self, event):
        super().resizeEvent(event)
        # You can add logic here to reposition items based on the new size