from component.button import ButtonElement
from component.modal import ConfirmationModal
from component.model import Answer
from component.text import TextElement
from component.button import ButtonElement,ButtonList
import os
from pydub import AudioSegment
from pydub.playback import play
from config.constant import color_dict
from config.constant import pofomopo_consonants,similarity_list
from config.dir import audio_dir
from storage.localStorage import dataHandaler
import pandas as pd
import random

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
            
class EndScreen(BaseScreen):
    def __init__(self, win,result):
        super().__init__(win)
        self.saveResult(result)
        self.add_element(TextElement(win, "Thank you for participating!", pos=(0, 0),color=color_dict["black"]))
        self.add_element(ButtonElement(win, "Replay", pos=(0, -0.2), width=0.3, height=0.2, color="green", action=self.replay))
        self.add_element(ButtonElement(win, "Quit", pos=(0, -0.5), width=0.3, height=0.2, color="red", action=self.quit))

    def replay(self,mouse):
        return StartScreen(self.win)

    def quit(self,mouse):
        return None  # This will end the experiment
    def saveResult(self,history):
        user_df = dataHandaler.get_user()
        user_df = user_df.drop(user_df.index)
        new_history_value = pd.DataFrame([element.to_dict() for element in history])
        new_history_value['participate_number'] = dataHandaler.get_new_sessionId()
        new_history_value = new_history_value.sort_values(by='question')
        user_df = pd.concat([user_df, pd.DataFrame([{"participantID":dataHandaler.get_new_sessionId()}])], ignore_index=True)
        dataHandaler.append_history_data(new_history_value)
        dataHandaler.append_user_data(user_df)


# StartScreen
class StartScreen(BaseScreen):
    def __init__(self, win):
        super().__init__(win)
        self.add_element(TextElement(win, "Quizz Experiment", pos=(0, 0),color=color_dict["black"]))
        self.add_element(ButtonElement(win, "Start", pos=(0, -0.2), width=0.3, height=0.2, color="green", action=self.navigate_start_screen))
        self.add_element(ButtonElement(win, "Setting", pos=(0, -0.5), width=0.3, height=0.2, color="blue", action=self.navigate_setting_screen))

    def navigate_setting_screen(self,mouse):
        return SettingScreen(self.win)
    
    def navigate_start_screen(self,mouse):
        return TestScreen(self.win)

# TestScreen
class TestScreen(BaseScreen):
    def __init__(self, win):
        super().__init__(win)
        self.answerList  = self.loadQuestion(audio_dir)
        self.current_index = 0
        # List of BofoMo consonants
        self.playSoundButton = ButtonElement(win, "Play Sound", pos=(-0.4, 0.5), width=0.4, height=0.2, color="blue", action=self.play_sound)
        self.previousButton  = ButtonElement(win, "Previous", pos=(0.55, -0.8), width=0.3, height=0.2, color="blue", action=self.previous_question)
        self.nextButton      = ButtonElement(win, "Next", pos=(0.85, -0.8), width=0.2, height=0.2, color="blue", action=self.next_question)
        self.submitButton    = ButtonElement(win, "Submit", pos=(0.7, -0.5), width=0.3, height=0.2, color="blue", action= self.submit_test)
        self.progress        = TextElement(win, "Test Number:{}/{}".format(self.current_index+1,len(self.answerList)), pos=(0.7, 0.9),color=color_dict["black"])
        self.bofomo_consonants_list  = ButtonList(
                                            win=win,
                                            textList=pofomopo_consonants,
                                            pos=(-0.32, -0.45),  # Grid position
                                            width=0.25,   # Button width
                                            height=0.2,  # Button height
                                            color="blue",  # Button color
                                            action=self.bofomo_consonant_action,   # Action to perform when a button is clicked
                                            rows=5,       # Number of rows
                                            columns=5,    # Number of columns
                                            horizontal_spacing=0.02,  # Horizontal spacing between buttons
                                            vertical_spacing=0.02      # Vertical spacing between buttons
                                        )
        self.similarities_list  = ButtonList(
                                            win=win,
                                            textList=similarity_list,
                                            pos=(0.8, 0.2),  # Grid position
                                            width=0.1,   # Button width
                                            height=0.15,  # Button height
                                            color="blue",  # Button color
                                            action=self.similarity_action,   # Action to perform when a button is clicked
                                            rows=5,       # Number of rows
                                            columns=1,    # Number of columns
                                            horizontal_spacing=0.01,  # Horizontal spacing between buttons
                                            vertical_spacing=0.01      # Vertical spacing between buttons
                                        )
        self.add_element(self.playSoundButton)
        self.add_element(self.submitButton)
        self.add_element(self.progress)
        self.add_element(self.bofomo_consonants_list)
        self.add_element(self.similarities_list)
        self.update_button_states()

        
    def next_question(self, mouse):
        self.current_index += 1
        self.update_button_states()
        self.updateProcess()
        return self
    
    def previous_question(self, mouse):
        self.current_index -= 1
        self.update_button_states()
        self.updateProcess()
        return self

    def play_sound(self, mouse):
        current_question = self.answerList[self.current_index]
        play(current_question.get_question())
        return self
        

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
        # Disable "Next" button when at the end
        if self.current_index == len(self.answerList) - 1:
            self.add_element(self.previousButton)
            self.remove_element(self.nextButton)
        elif  self.current_index == 0:
            self.add_element(self.nextButton)
            self.remove_element(self.previousButton)
        else:
            self.add_element(self.nextButton)
            self.add_element(self.previousButton)
        
        current_question = self.answerList[self.current_index]
        self.bofomo_consonants_list.updateState(current_question.get_answer())
        self.similarities_list.updateState(current_question.get_similarity())

    def submit_test(self, mouse):
        for  question in self.answerList:
            question.set_id(question.get_id()+1)
            question.set_answer(pofomopo_consonants[question.get_answer()] if question.get_answer()!= -1 else -1)
            question.set_similarity(similarity_list[question.get_similarity()] if question.get_similarity()!=-1 else -1)
        return EndScreen(self.win,self.answerList)
    
    def updateProcess(self):
        self.progress.set_text("Test Number:{}/{}".format(self.current_index+1,len(self.answerList)))
    
    # Action for BofoMo consonants
    def bofomo_consonant_action(self, button_index):
        current_question = self.answerList[self.current_index]
        current_question.set_answer(button_index)
        self.bofomo_consonants_list.updateState(button_index)
        return self

    # Action for similarities
    def similarity_action(self, button_index):
        current_question = self.answerList[self.current_index]
        current_question.set_similarity(button_index)
        self.similarities_list.updateState(button_index)
        return self


# Create the SettingScreen class with the Reset button and modal logic
class SettingScreen(BaseScreen):
    def __init__(self, win):
        super().__init__(win)
        self.add_element(TextElement(win, "Settings", pos=(0, 0), color=color_dict["black"]))
        self.add_element(ButtonElement(win, "Reset", pos=(0, -0.2), width=0.3, height=0.2, color="red",action=self.show_confirmation_modal))
        self.add_element(ButtonElement(win, "Back", pos=(0.7, -0.8), width=0.3, height=0.2, color="grey",action=self.navigate_main_screen))
        self.confirmation_modal = ConfirmationModal(win, "Are you sure you want to reset?",confirm_action=self.confirm,cancel_action=self.cancel)
        self.add_element(self.confirmation_modal)

    def show_confirmation_modal(self, mouse):
        self.confirmation_modal.visible = True
        return self
    
    def confirm(self, mouse):
        self.confirmation_modal.visible = False
        dataHandaler.resetHistory()
        return self

    def cancel(self, mouse):
        self.confirmation_modal.visible = False
        return self
    def navigate_main_screen(self,mouse):
        return StartScreen(self.win)