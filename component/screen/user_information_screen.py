
from component.field.user_infor import UserInfo
from component.modal import ConfirmDialog
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout,QHBoxLayout,QDialog
import logging
from model.session import currentSession

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
        self.user_info_fields = UserInfo(self)

        layout.addLayout(self.create_labeled_field("中文姓名", self.user_info_fields.chinese_name))
        layout.addLayout(self.create_labeled_field("英文姓名", self.user_info_fields.english_name))
        layout.addLayout(self.create_labeled_field("性別", self.user_info_fields.gender))
        layout.addLayout(self.create_labeled_field("出生年", self.user_info_fields.birth_year))
        layout.addLayout(self.create_labeled_field("教育程度", self.user_info_fields.education_level))
        layout.addLayout(self.create_labeled_field("母語", self.user_info_fields.native_language))
        layout.addLayout(self.create_labeled_field("跟家人常說語言", self.user_info_fields.family_language))
        layout.addLayout(self.create_labeled_field("跟朋友常說語言", self.user_info_fields.friend_language))


        # Save button
        save_btn = QPushButton('Save', self)
        save_btn.setStyleSheet("font-size: 18px; background-color: green; color: white; padding: 10px; margin-top: 15px;")
        save_btn.clicked.connect(self.show_confirm_dialog)
        layout.addWidget(save_btn)

        self.setLayout(layout)
        self.setWindowTitle('User Information')

    def save_data(self):
        user_info = self.user_info_fields.get_data()
        currentSession.set_user_info(user_info)

    def show_confirm_dialog(self):
        dialog = ConfirmDialog("save the information?",self)
        result = dialog.exec()

        if result == QDialog.DialogCode.Accepted:
            print("Save confirmed")
            self.save_data()
            self.navigator.navigate_to_test_screen()
        else:
            print("Save cancelled")



    def create_labeled_field(self, label_text: str, field: QWidget) -> QHBoxLayout:
        labeled_field_layout = QHBoxLayout()
        label = QLabel(label_text)
        labeled_field_layout.addWidget(label)
        labeled_field_layout.addWidget(field)
        return labeled_field_layout