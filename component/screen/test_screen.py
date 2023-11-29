
from component.model import Answer
import os
from storage.localStorage import dataHandaler
import random
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout,QProgressBar,QSizePolicy,QHBoxLayout,QSpacerItem, QGridLayout
import logging
from pydub.playback import play
from config.dir import audio_dir
from config.constant import pofomopo_consonants,similarity_list
from pydub import AudioSegment


# TestScreen
class TestScreen(QWidget):
    def __init__(self,navigator, screen_height, screen_width):
        super().__init__()
        self.navigator = navigator
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