from PyQt6.QtWidgets import QPushButton,QPushButton, QLabel, QVBoxLayout

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