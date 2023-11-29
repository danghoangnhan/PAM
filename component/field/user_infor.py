from PyQt6.QtWidgets import QLineEdit

class UserInfo:
    def __init__(self, parent=None):
        self.chinese_name = QLineEdit(parent)
        self.english_name = QLineEdit(parent)
        self.gender = QLineEdit(parent)
        self.birth_year = QLineEdit(parent)
        self.education_level = QLineEdit(parent)
        self.native_language = QLineEdit(parent)
        self.family_language = QLineEdit(parent)
        self.friend_language = QLineEdit(parent)

    def get_data(self)->dict:
        return {
            "中文姓名": self.chinese_name.text(),
            "英文姓名": self.english_name.text(),
            "性別": self.gender.text(),
            "出生年": self.birth_year.text(),
            "教育程度": self.education_level.text(),
            "母語": self.native_language.text(),
            "跟家人常說語言": self.family_language.text(),
            "跟朋友常說語言": self.friend_language.text()
        }
    