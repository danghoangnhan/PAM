import os
from component.modal import ConfirmDialog
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout,QTextEdit,QTabWidget,QDialog,QSpinBox,QComboBox,QHBoxLayout
from PyQt6.QtGui import QFont
from storage.localStorage import dataHandaler

import logging
from config.dir import keyboard_dir

class GeneralSettingTab(QWidget):
    def __init__(self, show_confirm_dialog_callback, keyboard_layout_list):
        super().__init__()
        main_layout = QVBoxLayout(self)

        # Similarities section
        similarities_layout = QHBoxLayout()
        similarities_label = QLabel("Similarities:")
        similarities_label.setFont(QFont("Arial", 16))  # Adjust font size
        similarities_layout.addWidget(similarities_label)
        self.similarities_spinbox = QSpinBox(self)
        self.similarities_spinbox.setFont(QFont("Arial", 16))  # Adjust font size
        self.similarities_spinbox.setMinimum(1)
        self.similarities_spinbox.setMaximum(15)
        self.similarities_spinbox.setValue(5)
        similarities_layout.addWidget(self.similarities_spinbox)
        main_layout.addLayout(similarities_layout)

        # Keyboard section
        keyboard_layout = QHBoxLayout()
        filenames_label = QLabel("Keyboard Label:")
        filenames_label.setFont(QFont("Arial", 16))  # Adjust font size
        keyboard_layout.addWidget(filenames_label)
        self.filenames_combobox = QComboBox(self)
        self.filenames_combobox.setFont(QFont("Arial", 16))  # Adjust font size
        self.filenames_combobox.addItems(keyboard_layout_list)
        keyboard_layout.addWidget(self.filenames_combobox)
        main_layout.addLayout(keyboard_layout)

        # Reset button
        reset_btn = QPushButton("Clear Csv Data", self)
        reset_btn.setFont(QFont("Arial", 16))  # Adjust font size
        reset_btn.clicked.connect(show_confirm_dialog_callback)
        main_layout.addWidget(reset_btn)

        self.setLayout(main_layout)


from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QLabel

class AboutTab(QWidget):
    def __init__(self, version, developer, designer):
        super().__init__()

        main_layout = QVBoxLayout(self)

        about_text = QTextEdit("Information about the app...")
        about_text.setReadOnly(True)
        main_layout.addWidget(about_text)

        version_label = QTextEdit(f"Version: {version}")
        version_label.setReadOnly(True)
        main_layout.addWidget(version_label)
        
        designer_label = QTextEdit(f"Designer: {designer}")
        designer_label.setReadOnly(True)
        main_layout.addWidget(designer_label)

        developer_label = QTextEdit(f"Developer: {developer}")
        developer_label.setReadOnly(True)
        main_layout.addWidget(developer_label)

        self.setLayout(main_layout)


        
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
        general_tab = GeneralSettingTab(show_confirm_dialog_callback=self.show_confirm_dialog,keyboard_layout_list=self.load_filenames())

        tab_widget.addTab(general_tab, "General")

        # Tab 2: About the App
        about_tab = AboutTab("1.3","DanielDu","Mannichu")
        tab_widget.addTab(about_tab, "About the App")

        back_btn = QPushButton("Back", self)
        back_btn.clicked.connect(self.navigator.navigate_to_start_screen)
        layout.addWidget(back_btn)

        self.setLayout(layout)

    def show_confirm_dialog(self):
        dialog = ConfirmDialog("Confirm Reset",self)
        result = dialog.exec()

        if result == QDialog.DialogCode.Accepted:
            print("Save confirmed")
            self.clear_csv_data()
        else:
            print("Save cancelled")
            self.cancel()

    def clear_csv_data(self):
        dataHandaler.resetHistory()

        print("Reset confirmed")

    def cancel(self):
        print("Reset cancelled")

    def load_filenames(self):
        filenames = os.listdir(keyboard_dir)
        return filenames

    