from component.modal import ConfirmDialog
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout,QTextEdit,QTabWidget,QDialog
import logging

class SettingScreen(QWidget):
    def __init__(self,navigator,screen_height,screen_width):
        super().__init__()
        logging.info("Initializing SettingScreen")
        
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.navigator = navigator

        self.resize(screen_height,screen_width)
        self.initUI()

    def initUI(self):
        logging.info("Setting up UI for SettingScreen")
        layout = QVBoxLayout(self)

        # Tab Widget
        tab_widget = QTabWidget(self)
        layout.addWidget(tab_widget)

        # Tab 1: General
        general_tab = QWidget()
        general_layout = QVBoxLayout(general_tab)

        reset_btn = QPushButton("Reset", general_tab)
        reset_btn.clicked.connect(self.show_confirm_dialog)
        general_layout.addWidget(reset_btn)

        general_tab.setLayout(general_layout)
        tab_widget.addTab(general_tab, "General")

        # Tab 2: About the App
        about_tab = QWidget()
        about_layout = QVBoxLayout(about_tab)

        about_text = QTextEdit("Information about the app...")
        about_text.setReadOnly(True)
        about_layout.addWidget(about_text)

        about_tab.setLayout(about_layout)
        tab_widget.addTab(about_tab, "About the App")


        
        layout.addWidget(QLabel("Settings"))

        reset_btn = QPushButton("Reset", self)
        reset_btn.clicked.connect(self.show_confirm_dialog)
        layout.addWidget(reset_btn)

        back_btn = QPushButton("Back", self)
        back_btn.clicked.connect(self.navigator.navigate_to_start_screen)
        layout.addWidget(back_btn)

        self.setLayout(layout)

    def show_confirm_dialog(self):
        dialog = ConfirmDialog(self)
        result = dialog.exec()

        if result == QDialog.DialogCode.Accepted:
            print("Save confirmed")
            self.confirm()
        else:
            print("Save cancelled")
            self.cancel()

    def confirm(self):
        print("Reset confirmed")

    def cancel(self):
        print("Reset cancelled")

    # def navigate_main_screen(self):
    #     logging.info("Open the user start screen")
    #     self.next_screen = StartScreen(self.screen_height,self.screen_width)
    #     self.next_screen.show()
    #     self.close()

    