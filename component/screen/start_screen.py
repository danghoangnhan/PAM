import logging
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton,QLabel,QSizePolicy
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

        # Add stretch to center the widgets vertically
        layout.addStretch()

        # Title
        title = QLabel("Quiz Experiment", self)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold;")  # Increase font size and make it bold
        layout.addWidget(title)

        # Start button
        start_btn = QPushButton("Start", self)
        start_btn.clicked.connect(self.navigator.navigate_to_user_info_screen)
        start_btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        start_btn.setStyleSheet("background-color: green; color: white; font-size: 20px; padding: 10px;")
        layout.addWidget(start_btn)

        # Settings button
        settings_btn = QPushButton("Settings", self)
        settings_btn.clicked.connect(self.navigator.navigate_to_setting_screen)
        settings_btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        settings_btn.setStyleSheet("background-color: gray; color: white; font-size: 20px; padding: 10px;")
        layout.addWidget(settings_btn)

        # Add another stretch to ensure buttons are centered
        layout.addStretch()

        self.setLayout(layout)
        self.setWindowTitle('Start Screen')