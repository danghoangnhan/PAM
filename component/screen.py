from component.modal import ConfirmDialog
from component.model import Answer
import os
from pydub import AudioSegment
from pydub.playback import play
from config.constant import pofomopo_consonants,similarity_list
from config.dir import audio_dir
from storage.localStorage import dataHandaler
import pandas as pd
import random
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,QDialog,QProgressBar,QGridLayout,QSizePolicy,QHBoxLayout,QSpacerItem
from PyQt6.QtCore import Qt

import logging

class BaseScreen:
    def __init__(self, win):
        self.win = win
        self.elements = []

    def add_element(self, element):
        if element not in self.elements:
            self.elements.append(element)

    def remove_element(self, element):
        if element in self.elements:
            self.elements.remove(element)
            
    def draw(self):
        for element in self.elements:
            element.draw()

            
class EndScreen(QWidget,):
    def __init__(self,screen_height,screen_width, result):
        super().__init__()
        
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.resize(screen_height,screen_width)

        self.result = result
        self.initUI()
        self.saveResult(result)

    def initUI(self):
        layout = QVBoxLayout(self)

        # Thank you message
        thank_you_label = QLabel("Thank you for participating!", self)
        layout.addWidget(thank_you_label)

        # Replay button
        replay_btn = QPushButton("Replay", self)
        replay_btn.clicked.connect(self.navigate_start_screen)
        layout.addWidget(replay_btn)

        # Quit button
        quit_btn = QPushButton("Quit", self)
        quit_btn.clicked.connect(self.quit)
        layout.addWidget(quit_btn)

        self.setLayout(layout)


    def navigate_start_screen(self):
        logging.info("Open the StartScreen")
        self.next_screen = StartScreen(self.screen_height,self.screen_width)
        self.next_screen.show()
        self.close()

    def quit(self):
        # Logic to quit the experiment
        self.close()  # Closes the EndScreen window

    def saveResult(self,history):
        user_df = dataHandaler.get_user()
        user_df = user_df.drop(user_df.index)
        new_history_value = pd.DataFrame([element.to_dict() for element in history])
        new_history_value['participate_number'] = dataHandaler.get_new_sessionId()
        new_history_value = new_history_value.sort_values(by='question')
        user_df = pd.concat([user_df, pd.DataFrame([{"participantID":dataHandaler.get_new_sessionId()}])], ignore_index=True)
        dataHandaler.append_history_data(new_history_value)
        dataHandaler.append_user_data(user_df)

class StartScreen(QWidget):
    def __init__(self,screen_height,screen_width):
        super().__init__()
        self.screen_height = screen_height
        self.screen_width = screen_width
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
        start_btn.clicked.connect(self.navigate_UserInformationScreen_screen)
        start_btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        start_btn.setStyleSheet("background-color: green; color: white; font-size: 20px; padding: 10px;")
        layout.addWidget(start_btn)

        # Settings button
        settings_btn = QPushButton("Settings", self)
        settings_btn.clicked.connect(self.navigate_setting_screen)
        settings_btn.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        settings_btn.setStyleSheet("background-color: gray; color: white; font-size: 20px; padding: 10px;")
        layout.addWidget(settings_btn)

        # Add another stretch to ensure buttons are centered
        layout.addStretch()

        self.setLayout(layout)
        self.setWindowTitle('Start Screen')

    def navigate_setting_screen(self):
        logging.info(" Open the settings screen")
        self.next_screen = SettingScreen(self.screen_height,self.screen_width)
        self.next_screen.show()
        self.close()

    def navigate_UserInformationScreen_screen(self):
        logging.info("Open the user information screen")
        self.user_info_screen = UserInformationScreen(self.screen_height,self.screen_width)
        self.user_info_screen.show()
        self.close()

# TestScreen
class TestScreen(QWidget):
    def __init__(self, screen_height, screen_width):
        super().__init__()
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.resize(screen_width, screen_height)
        self.setWindowTitle("Test Screen")
        logging.info("Initializing TestScreen")
        self.initUI()
        self.answerList = self.loadQuestion(audio_dir)
        self.current_index = 0
        self.updateProcess()
        self.update_button_states()

        self.answerList  = self.loadQuestion(audio_dir)
        self.current_index = 0

    def initUI(self):
        logging.info("Setting up UI for TestScreen")
        
        layout = QVBoxLayout(self)

        self.progress_label = QLabel("Test Number: 0/0")
        layout.addWidget(self.progress_label)

        self.playSoundButton = QPushButton("Play Sound")
        self.playSoundButton.clicked.connect(self.play_sound)
        layout.addWidget(self.playSoundButton)

        self.progress_bar = QProgressBar(self)
        
        button_layout = QHBoxLayout()

         # Spacer to push buttons to the right
        spacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        button_layout.addItem(spacer)

        # Previous Button
        self.previousButton = QPushButton("Previous")
        self.previousButton.clicked.connect(self.previous_question)
        button_layout.addWidget(self.previousButton)

        # Next Button
        self.nextButton = QPushButton("Next")
        self.nextButton.clicked.connect(self.next_question)
        button_layout.addWidget(self.nextButton)

        # Submit Button
        submitButton = QPushButton("Submit")
        submitButton.clicked.connect(self.handling_submit_button)
        button_layout.addWidget(submitButton)

        # Add the horizontal layout to the main layout

        layout.addLayout(button_layout)
        self.setLayout(layout)
        self.setWindowTitle('TestScreen')

        
        # Create grid layout for bofomo consonants
        self.bofomo_consonants_grid = QGridLayout()
        for i, text in enumerate(pofomopo_consonants):
            button = QPushButton(str(text), self)
            button.clicked.connect(lambda checked, text=text: self.bofomo_consonant_action(text))
            row, col = divmod(i, 5)
            self.bofomo_consonants_grid.addWidget(button, row, col)
        layout.addLayout(self.bofomo_consonants_grid)

        # Create grid layout for similarities
        self.similarities_grid = QGridLayout()
        for i, text in enumerate(similarity_list):
            button = QPushButton(str(text), self)
            button.clicked.connect(lambda checked, text=text: self.similarity_action(text))
            row, col = divmod(i, 1)
            self.similarities_grid.addWidget(button, row, col)
        layout.addLayout(self.similarities_grid)

    def next_question(self):
        self.current_index += 1
        self.update_button_states()
        self.updateProcess()
    
    def previous_question(self):
        self.current_index -= 1
        self.update_button_states()
        self.updateProcess()

    def play_sound(self):
        current_question = self.answerList[self.current_index]
        play(current_question.get_question())
        

    def loadQuestion(self, audio_dir):
        question_df = dataHandaler.get_exam()
        quetionList = []
        for index, row in question_df.iterrows():
            filename = row['path']
            filename = os.path.join(audio_dir, filename)
            sound_file = AudioSegment.from_file(file = os.path.join(audio_dir, filename))
            answer = Answer(question=sound_file,id=index)
            quetionList.append(answer)
        random.shuffle(quetionList)
        return quetionList
    
    def update_button_states(self):

        is_first_question = self.current_index == 0
        is_last_question = self.current_index == len(self.answerList) - 1

        self.previousButton.setVisible(not is_first_question)
        self.nextButton.setVisible(not is_last_question)
        
        current_question = self.answerList[self.current_index]

    def handling_submit_button(self):
        self.submit_test()
        self.navigate_end_screen()

    def submit_test(self):
        for  question in self.answerList:
            question.set_id(question.get_id()+1)
            question.set_answer(pofomopo_consonants[question.get_answer()] if question.get_answer()!= -1 else -1)
            question.set_similarity(similarity_list[question.get_similarity()] if question.get_similarity()!=-1 else -1)


    def navigate_end_screen(self):
        logging.info("Open the EndScreen")
        self.next_screen = EndScreen(self.screen_height,self.screen_width,self.answerList)
        self.next_screen.show()
        self.close()
    
    def updateProcess(self):
        # Update the progress label
        self.progress_label.setText(f"Test Number: {self.current_index + 1}/{len(self.answerList)}")
        
        # Update the progress bar
        if len(self.answerList) > 0:
            progress_value = int((self.current_index + 1) / len(self.answerList) * 100)
            self.progress_bar.setValue(progress_value)
        else:
            self.progress_bar.setValue(0)
        # self.progress.set_text("Test Number:{}/{}".format(self.current_index+1,len(self.answerList)))
    
    # Action for BofoMo consonants
    def bofomo_consonant_action(self, button_index):
        current_question = self.answerList[self.current_index]
        current_question.set_answer(button_index)
        # self.bofomo_consonants_list.updateState(button_index)

    # Action for similarities
    def similarity_action(self, button_index):
        current_question = self.answerList[self.current_index]
        current_question.set_similarity(button_index)
        # self.similarities_list.updateState(button_index)


class SettingScreen(QWidget):
    def __init__(self,screen_height,screen_width):
        super().__init__()
        logging.info("Initializing SettingScreen")
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.resize(screen_height,screen_width)
        self.initUI()

    def initUI(self):
        logging.info("Setting up UI for SettingScreen")
        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("Settings"))

        reset_btn = QPushButton("Reset", self)
        reset_btn.clicked.connect(self.show_confirm_dialog)
        layout.addWidget(reset_btn)

        back_btn = QPushButton("Back", self)
        back_btn.clicked.connect(self.navigate_main_screen)
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

    def navigate_main_screen(self):
        logging.info("Open the user start screen")
        self.next_screen = StartScreen(self.screen_height,self.screen_width)
        self.next_screen.show()
        self.close()

    
class UserInformationScreen(QWidget):
    def __init__(self,screen_height,screen_width):
        super().__init__()
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.resize(screen_height,screen_width)
        logging.info("Initializing UserInformationScreen")
        self.initUI()

    def initUI(self):
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
            self.navigate_test_screen()
        else:
            print("Save cancelled")