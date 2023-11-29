from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,QDialog,QProgressBar,QGridLayout,QSizePolicy,QHBoxLayout,QSpacerItem,QTabWidget,QTextEdit
from PyQt6.QtCore import Qt

class BaseScreen(QWidget):
    def __init__(self,screen_height,screen_width):
            super().__init__()
            
            self.screen_height = screen_height
            self.screen_width = screen_width
            self.resize(screen_height,screen_width)

    def initUI(self):
        pass
