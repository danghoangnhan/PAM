from component.button import ButtonElement
from component.model import Answer
from component.text import TextElement
from component.button import ButtonElement
from time import time

import os
from config.dir import data_dir
from pydub import AudioSegment
from pydub.playback import play
from config.font import color_dict

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
    def __init__(self, win):
        super().__init__(win)
        self.add_element(TextElement(win, "Thank you for participating!", pos=(0, 0)))
        self.add_element(ButtonElement(win, "Replay", pos=(0, -0.2), width=0.2, height=0.1, color="green", action=self.replay))
        self.add_element(ButtonElement(win, "Quit", pos=(0, -0.4), width=0.2, height=0.1, color="red", action=self.quit))

    def replay(self):
        return StartScreen(self.win)

    def quit(self):
        return None  # This will end the experiment

# StartScreen
class StartScreen(BaseScreen):
    def __init__(self, win):
        super().__init__(win)
        self.add_element(TextElement(win, "Test Name", pos=(0, 0)))
        self.add_element(ButtonElement(win, "Start", pos=(0, -0.2), width=0.2, height=0.1, color="green", action=self.next_screen))

    def next_screen(self):
        return TestScreen(self.win)

# TestScreen
class TestScreen(BaseScreen):
    def __init__(self, win):
        super().__init__(win)
        self.answerList  = self.get_m4a_files(data_dir)
        
        self.playSoundButton = ButtonElement(win, "Play Sound", pos=(-0.2, 0.2), width=0.2, height=0.1, color="blue", action=self.play_sound)
        self.previousButton  = ButtonElement(win, "Previous", pos=(0.5, -0.8), width=0.3, height=0.2, color="blue", action=self.debounce(self.previous_question))
        self.nextButton      = ButtonElement(win, "Next", pos=(0.85, -0.8), width=0.2, height=0.2, color="blue", action=self.debounce(self.next_question))
        self.submitButton    = ButtonElement(win, "Submit", pos=(0.7, -0.5), width=0.3, height=0.2, color="blue", action= self.submit_test)
        self.progress        = TextElement(win, "Test Number:{}/{}".format(0,len(self.answerList)), pos=(0.7, 0.9),color=color_dict["black"])
        
        self.add_element(self.playSoundButton)
        self.add_element(self.submitButton)
        self.add_element(self.progress)
        
        self.current_index = 0
        self.update_button_states()
        # Initialize debounce timer
        self.debounce_timer = None
        
    def next_question(self):
        self.current_index += 1
        print("increase")
        self.update_button_states()
        self.updateProcess()
        return self
    def previous_question(self):
        self.current_index -= 1
        print("decrease")
        self.update_button_states()
        self.updateProcess()
        return self
        
    def play_sound(self):
        current_question = self.answerList[self.current_index]
        play(current_question.get_question())
        return self
        

    def get_m4a_files(self, directory):
        quetionList = []
        for filename in os.listdir(directory):
            filename = os.path.join(directory, filename)
            sound_file = AudioSegment.from_file(file = os.path.join(directory, filename))
            quetionList.append(Answer(question=sound_file))
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
            
    def submit_test(self):
        return EndScreen(self.win)
    
    def updateProcess(self):
        self.progress.set_text("{}/{}".format(self.current_index+1,len(self.answerList)))
    
     

    def debounce(self, func):
        def wrapped_func():
            if self.debounce_timer is None or time() - self.debounce_timer >= 0.5:  # Adjust debounce time as needed
                self.debounce_timer = time()
                func()