import logging
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton,QLabel,QSizePolicy,QSpacerItem
from PyQt6.QtCore import Qt

class StartScreen(QWidget):
    def __init__(self,navigator,screen_height,screen_width):
        super().__init__()
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.navigator = navigator
        self.resize(screen_height,screen_width)
        logging.info("Initializing StartScreen")
        self.initUI()

    def initUI(self):
        logging.info("Setting up UI for StartScreen")
        
        layout = QVBoxLayout()
        spacer_left = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)
        spacer_right = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)
        layout.addItem(spacer_left)
        # Add stretch to center the widgets vertically
        layout.addStretch()

        # Title
        title = QLabel("PAMSimulator", self)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold;")  # Increase font size and make it bold
        layout.addWidget(title)

        # Start button
        start_btn = QPushButton("Start", self)
        start_btn.clicked.connect(self.navigator.navigate_to_user_info_screen)
        start_btn.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        start_btn.setStyleSheet("background-color: green; color: white; font-size: 20px; padding: 10px;")
        layout.addWidget(start_btn)

        # Settings button
        settings_btn = QPushButton("Settings", self)
        settings_btn.clicked.connect(self.navigator.navigate_to_setting_screen)
        settings_btn.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        settings_btn.setStyleSheet("background-color: gray; color: white; font-size: 20px; padding: 10px;")
        layout.addWidget(settings_btn)

        # Add another stretch to ensure buttons are centered
        layout.addStretch()
        layout.addItem(spacer_right)
        self.setLayout(layout)
        self.setWindowTitle('Start Screen')