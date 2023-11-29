
from component.button import SquareButton
from component.model import Answer
import os
from storage.localStorage import dataHandaler
import random
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout,QProgressBar,QSizePolicy,QHBoxLayout,QSpacerItem, QGridLayout
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt,QSize
from typing import List

import logging
from pydub.playback import play
from config.dir import audio_dir
from config.constant import pofomopo_consonants,similarity_list
from pydub import AudioSegment
from config.dir import volume_icon

# TestScreen
class TestScreen(QWidget):
    def __init__(self,navigator, screen_height, screen_width):
        super().__init__()
        self.navigator = navigator
        self.screen_height = screen_height
        self.screen_width = screen_width
        self.resize(screen_height,screen_width)
        self.keyboard_list:List[QPushButton] = []
        self.similarities_list = []
        self.setWindowTitle("Test Screen")
        logging.info("Initializing TestScreen")
        
        self.initUI()
        self.answerList:List[Answer] = self.loadQuestion(audio_dir)
        self.current_index:int = 0
        self.updateProcess()
        self.update_button_states()


    def initUI(self):
        logging.info("Setting up UI for TestScreen")
        
        main_layout = QVBoxLayout(self)

        #Grid 1: Audio and Progress
        grid1_layout = QHBoxLayout()
        grid1_1_layout = QVBoxLayout()
        self.progress_label = QLabel("Test Number: 0/0")
        self.progress_label.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        grid1_1_layout.addWidget(self.progress_label)

        # self.progress_bar = QProgressBar(self)
        # grid1_1_layout.addWidget(self.progress_bar)

        self.playSoundButton = SquareButton(QIcon(volume_icon), "Play Sound",self)
        self.playSoundButton.clicked.connect(self.play_sound)
        self.playSoundButton.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        grid1_layout.addWidget(self.playSoundButton)

        
        grid1_layout.addLayout(grid1_1_layout)
        main_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum))

        main_layout.addLayout(grid1_layout)


        grid2_layout = QHBoxLayout(self)        
        self.bofomo_consonants_grid = QGridLayout()
        self.bofomo_consonants_grid.setHorizontalSpacing(0)
        self.bofomo_consonants_grid.setVerticalSpacing(0)
        button_size = QSize(80, 80)  # Adjust the size as needed

        for i, text in enumerate(pofomopo_consonants):
            button = QPushButton(str(text), self)
            self.keyboard_list.append(button)
            button.clicked.connect(lambda checked, text=text: self.bofomo_consonant_action(text))
            button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
            button.setMinimumSize(button_size)
            row, col = divmod(i, 5)
            self.bofomo_consonants_grid.addWidget(button, row, col)
        grid2_layout.addLayout(self.bofomo_consonants_grid)

        self.similarities_grid = QGridLayout()
        button_size = QSize(80, 80)  # Adjust the size as needed
        for i, text in enumerate(similarity_list):
            button = QPushButton(str(text), self)
            self.similarities_list.append(button)
            button.clicked.connect(lambda checked, text=text: self.similarity_action(text))
            button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
            button.setMinimumSize(button_size)
            row, col = divmod(i, 1)
            self.similarities_grid.addWidget(button, row, col)
        spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        grid2_layout.addItem(spacer)

        grid2_layout.addLayout(self.similarities_grid)
        main_layout.addLayout(grid2_layout)

        grid3 = QVBoxLayout()
        grid_3_1 = QHBoxLayout()

        # Previous Button
        self.previousButton = QPushButton("Previous")
        self.previousButton.clicked.connect(self.previous_question)
        grid_3_1.addWidget(self.previousButton)

        # Next Button
        self.nextButton = QPushButton("Next")
        self.nextButton.clicked.connect(self.next_question)
        grid_3_1.addWidget(self.nextButton)

        # Submit Button
        submitButton = QPushButton("Submit")
        submitButton.clicked.connect(self.handling_submit_button)
        grid3.addWidget(submitButton)
        grid3.addLayout(grid_3_1)

        # Add the horizontal layout to the main layout
        main_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        main_layout.addLayout(grid3)


        self.setLayout(main_layout)
        self.setWindowTitle('TestScreen')

    def next_question(self):
        self.current_index += 1
        self.update_button_states()
        self.updateProcess()
    
    def previous_question(self):
        self.current_index -= 1
        self.update_button_states()
        self.updateProcess()

    def play_sound(self):
        current_question:Answer = self.answerList[self.current_index]
        play(current_question.get_question())
        

    def loadQuestion(self, audio_dir)->List[Answer]:
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
        
        current_question:Answer = self.answerList[self.current_index]
        for button in self.keyboard_list:
            if button.text() == current_question.get_answer():
                self.update_button_style(button)
            else:
                self.reset_button_style(button)
        for button in self.similarities_list:
            if button.text() == current_question.get_similarity():
                self.update_button_style(button)
            else:
                self.reset_button_style(button)
        
        print(current_question.get_answer())
        print(current_question.get_similarity())
        
    def handling_submit_button(self):
        self.submit_test()
        self.navigator.navigate_to_end_screen()

    def submit_test(self):
        for  question in self.answerList:
            question.set_id(question.get_id()+1)
            question.set_answer(pofomopo_consonants[question.get_answer()] if question.get_answer()!= -1 else -1)
            question.set_similarity(similarity_list[question.get_similarity()] if question.get_similarity()!=-1 else -1)

    
    def updateProcess(self):
        # Update the progress label
        self.progress_label.setText(f"Test Number: {self.current_index + 1}/{len(self.answerList)}")
        
        # Update the progress bar
        # if len(self.answerList) > 0:
        #     progress_value = int((self.current_index + 1) / len(self.answerList) * 100)
        #     self.progress_bar.setValue(progress_value)
        # else:
        #     self.progress_bar.setValue(0)
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


    def update_button_style(self, button):
        button.setStyleSheet("background-color: #D3D3D3")

    def reset_button_style(self, button):
        button.setStyleSheet("")