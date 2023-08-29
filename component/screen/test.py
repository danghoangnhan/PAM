from component.button import ButtonElement
# from pydub import AudioSegment
# from psychopy import sound
import os
from config.dir import data_dir
from component.screen.base import BaseScreen
from pydub import AudioSegment
from pydub.playback import play


class Answer:
    def __init__(self, question):
        self.question = question
        self.answer = None
        self.similarity = None

    # Setter method for 'answer'
    def set_answer(self, answer):
        self.answer = answer

    # Getter method for 'answer'
    def get_answer(self):
        return self.answer

    # Setter method for 'similarity'
    def set_similarity(self, similarity):
        self.similarity = similarity

    # Getter method for 'similarity'
    def get_similarity(self):
        return self.similarity

    # Setter method for 'question'
    def set_question(self, question):
        self.question = question

    # Getter method for 'question'
    def get_question(self):
        return self.question

# TestScreen
class TestScreen(BaseScreen):
    def __init__(self, win):
        super().__init__(win)
        self.answerList  = self.get_m4a_files(data_dir)
        self.add_element(ButtonElement(win, "Play Sound", pos=(-0.4, 0.2), width=0.2, height=0.1, color="blue", action=self.play_sound))
        self.currentAnswer = self.answerList[0]

    def play_sound(self):
        if self.currentAnswer is not None:
            print(self.currentAnswer.get_question())
            play(self.currentAnswer.get_question())

    def set_currentAnswer(self, answer):
        self.currentAnswer = answer

    def get_m4a_files(self, directory):
        quetionList = []
        for filename in os.listdir(directory):
            audio = AudioSegment.from_file(os.path.join(directory, filename))
            quetionList.append(Answer(question=audio))
        return quetionList

