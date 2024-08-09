from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QPushButton, QSizePolicy

from app.utils.constants import Colors


class OptionsView(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.setStyleSheet("border: 0")
        self.load_view()

    def load_view(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(10, 0, 0, 10)
        main_layout.setSpacing(10)

        grid_layout = QGridLayout()

        font = QFont("Arial", 24)

        # Create buttons
        send_order_button = QPushButton("Trimite Comanda")
        send_order_button.setObjectName("send_order_button")
        send_order_button.setStyleSheet(f"""
            QPushButton#send_order_button {{
                background-color: {Colors.LIGHT_GREEN};
                color: {Colors.WHITE};
                border-radius: 5px;
            }}""")
        send_order_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        send_order_button.setFont(font)

        bill_button = QPushButton("Nota Plata")
        bill_button.setObjectName("bill_button")
        bill_button.setStyleSheet(f"""
                    QPushButton#bill_button {{
                        background-color: {Colors.LIGHT_GREEN};
                        color: {Colors.WHITE};
                        border-radius: 5px;
                    }}""")
        bill_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        bill_button.setFont(font)

        fiscal_receipt_button = QPushButton("Bon Fiscal")
        fiscal_receipt_button.setObjectName("fiscal_receipt_button")
        fiscal_receipt_button.setStyleSheet(f"""
                    QPushButton#fiscal_receipt_button {{
                        background-color: {Colors.LIGHT_GREEN};
                        color: {Colors.WHITE};
                        border-radius: 5px;
                    }}""")
        fiscal_receipt_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        fiscal_receipt_button.setFont(font)

        # Add buttons to grid layout
        grid_layout.addWidget(send_order_button, 0, 0, 1, 2)
        grid_layout.addWidget(bill_button, 1, 0, 1, 1)
        grid_layout.addWidget(fiscal_receipt_button, 1, 1, 1, 1)

        grid_layout.setColumnStretch(0, 1)
        grid_layout.setColumnStretch(1, 1)

        grid_layout.setRowStretch(0, 1)
        grid_layout.setRowStretch(1, 1)



        main_layout.addLayout(grid_layout)
        self.setLayout(main_layout)