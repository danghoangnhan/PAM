from PyQt6.QtWidgets import QPushButton,QApplication,QPushButton, QLabel, QVBoxLayout, QApplication
from PyQt6.QtCore import QSize,Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize


class SquareButton(QPushButton):
    def __init__(self, icon, text, parent=None):
        super().__init__("", parent)  # Initialize without text

        # Create the icon and text label
        self.icon_label = QLabel()
        self.icon_label.setPixmap(icon.pixmap(50, 50))  # Set icon size
        self.text_label = QLabel(text)
        self.setFixedSize(100, 100)
        # Create a vertical layout to stack icon and text
        layout = QVBoxLayout()
        layout.addWidget(self.icon_label)
        layout.addWidget(self.text_label)
        self.setLayout(layout)

    # def sizeHint(self):
    #     screen = QApplication.screens()[0]
    #     screen_size = screen.availableGeometry()
    #     # Calculate the button size based on screen size
    #     button_size = screen_size.width() / 10
    #     return QSize(button_size, button_size)