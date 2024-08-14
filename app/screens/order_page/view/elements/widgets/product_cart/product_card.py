from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtWidgets import QPushButton, QGridLayout, QWidget, QSizePolicy, QLabel, QVBoxLayout

from app.screens.order_page.model.product import Product
from app.utils.constants import Colors


class ProductCardWidget(QPushButton):
    def __init__(self, product, parent=None):
        super().__init__(parent)
        self.product: Product = product
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setStyleSheet("""
            QPushButton {
                border: none;
            }
        """)

        self.init_ui()

    def init_ui(self):
        self.layout = QGridLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.create_image_widget()
        self.create_label_widget()

        self.layout.setRowStretch(0, 8)
        self.layout.setRowStretch(1, 4)

    def create_image_widget(self):
        self.build_image_widget()
        self.layout.addWidget(self.image_widget)

    def build_image_widget(self):
        self.image_widget = QWidget()
        self.image_widget.setObjectName("image_widget")
        self.image_widget.setStyleSheet(f"""
                #image_widget {{
                    background-color: {Colors.SOFT_BLUE_2};
                    border: 1px solid {Colors.SOFT_BLUE};
                    border-radius: 5px;
                    }}
                """)
        self.image_widget.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        main_layout = QGridLayout(self.image_widget)
        image_label = self.create_image_label()
        main_layout.addWidget(image_label, 0, 0, Qt.AlignmentFlag.AlignCenter)


    def create_image_label(self):
        pixmap = QPixmap('static/ProductCardDefault_blue.png')
        scaled_pixmap = pixmap.scaled(QSize(self.image_widget.size().width() // 6, self.image_widget.size().height() // 6), Qt.AspectRatioMode.KeepAspectRatio,
                                      Qt.TransformationMode.SmoothTransformation)
        image_label = QLabel()
        image_label.setPixmap(scaled_pixmap)
        image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        return image_label

    def create_label_widget(self):
        label_widget = self.build_label_widget()
        self.layout.addWidget(label_widget)

    def build_label_widget(self):
        label_widget = QWidget()
        label_widget.setObjectName("label_widget")
        label_layout = QGridLayout(label_widget)
        label_layout.setContentsMargins(5, 10, 0, 0)
        label_layout.setSpacing(0)

        product_name_widget = self.create_product_name_widget()
        if self.product.id != -1:
            label_layout.addWidget(product_name_widget, 0, 0, Qt.AlignmentFlag.AlignLeft)

        return label_widget

    def create_product_name_widget(self):
        product_name_widget = QWidget()
        product_name_layout = QGridLayout(product_name_widget)
        product_name_layout.setContentsMargins(0, 0, 0, 0)
        product_name_layout.setSpacing(10)

        svg_widget = self.create_svg_widget()
        label1 = self.create_label(self.product.name, 20, False)
        label2 = self.create_label(f"{self.product.price:.2f} RON", 20, True)

        product_name_layout.addWidget(svg_widget, 0, 0, Qt.AlignmentFlag.AlignLeft)
        product_name_layout.addWidget(label1, 0, 1, Qt.AlignmentFlag.AlignLeft)
        product_name_layout.addWidget(label2, 1, 1, Qt.AlignmentFlag.AlignLeft)

        return product_name_widget

    def create_svg_widget(self):
        svg_widget = QSvgWidget()
        svg_widget.load("static/icons/arrow/arrow_1.svg")
        svg_widget.setFixedSize(20, 20)
        svg_widget.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        return svg_widget

    def create_label(self, text, font_size, bold):
        font = QFont("Arial", font_size, QFont.Weight.Bold if bold else QFont.Weight.Normal)
        label = QLabel(text)
        label.setFont(font)
        label.setStyleSheet("color: black;")
        label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        return label

class ProductCardContainer(QWidget):
    def __init__(self, product, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 10, 0, 0)  # Set margin-top to 10px
        self.product_card = ProductCardWidget(product)
        self.product_card.setObjectName("product_card")
        self.layout.addWidget(self.product_card)

        self.setStyleSheet(f"""
                        #product_card {{
                            background-color: {Colors.MEDIUM_GRAY};
                            }}""")