from storage.localStorage import dataHandaler
import pandas as pd
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
import logging
from PyQt6.QtCore import Qt


class EndScreen(QWidget,):
    def __init__(self,navigator,screen_height,screen_width, result):
        super().__init__()
        
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.navigator = navigator

        self.resize(screen_height,screen_width)

        self.result = result
        self.initUI()
    
    def initUI(self):
        layout = QVBoxLayout(self)

        # Thank you message
        thank_you_label = QLabel("Thank you for participating!", self)

        thank_you_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        thank_you_label.setStyleSheet("font-size: 24px; font-weight: bold;")  # Increase font size and make it bold
        layout.addWidget(thank_you_label)

        # Replay button
        replay_btn = QPushButton("Replay", self)
        replay_btn.clicked.connect(self.navigator.navigate_to_start_screen)
        # settings_btn.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        replay_btn.setStyleSheet("background-color: green; color: white; font-size: 20px; padding: 10px;")
        layout.addWidget(replay_btn)

        # Quit button
        quit_btn = QPushButton("Quit", self)
        quit_btn.clicked.connect(self.navigator.close_all)
        quit_btn.setStyleSheet("background-color: red; color: white; font-size: 20px; padding: 10px;")
        layout.addWidget(quit_btn)

        self.setLayout(layout)