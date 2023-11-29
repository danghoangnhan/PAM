
from component.modal import ConfirmDialog
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout,QLineEdit,QDialog
import logging

class UserInformationScreen(QWidget):
    def __init__(self,navigator,screen_height:int,screen_width:int):
        super().__init__()
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.navigator = navigator
        self.resize(screen_height,screen_width)
        logging.info("Initializing UserInformationScreen")
        self.initUI()

    def initUI(self)->None:
        logging.info("Setting up UI for StartScreen")
        layout = QVBoxLayout()
        # Labels and fields
        self.fields = {
            "中文姓名": QLineEdit(self),
            "英文姓名": QLineEdit(self),
            "性別": QLineEdit(self),
            "出生年": QLineEdit(self),
            "教育程度": QLineEdit(self),
            "母語": QLineEdit(self),
            "跟家人常說語言": QLineEdit(self),
            "跟朋友常說語言": QLineEdit(self)
        }

        for label, edit in self.fields.items():
            layout.addWidget(QLabel(label))
            layout.addWidget(edit)

        # Save button
        save_btn = QPushButton('Save', self)
        save_btn.setStyleSheet("font-size: 18px; background-color: green; color: white; padding: 10px; margin-top: 15px;")
        save_btn.clicked.connect(self.show_confirm_dialog)
        layout.addWidget(save_btn)

        self.setLayout(layout)
        self.setWindowTitle('User Information')

    def save_data(self):
        user_info = {label: edit.text() for label, edit in self.fields.items()}
        print("User Info Saved:", user_info)
    
    def navigate_test_screen(self):
        logging.info("Open the TestScreen")
        self.test_screen = TestScreen(self.screen_height,self.screen_width)
        self.test_screen.show()
        self.close()

    def show_confirm_dialog(self):
        dialog = ConfirmDialog(self)
        result = dialog.exec()

        if result == QDialog.DialogCode.Accepted:
            print("Save confirmed")
            self.save_data()
            # self.navigator
            self.navigate_test_screen()
        else:
            print("Save cancelled")