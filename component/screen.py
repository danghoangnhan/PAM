from component.button import ButtonElement
from component.model import Answer
from component.text import TextElement
from component.button import ButtonElement,ButtonList
import os
from pydub import AudioSegment
from pydub.playback import play
from config.constant import color_dict
from config.constant import pofomopo_consonants,similarity_list
from config.dir import audio_dir

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
        self.add_element(TextElement(win, "Thank you for participating!", pos=(0, 0),color=color_dict["black"]))
        self.add_element(ButtonElement(win, "Replay", pos=(0, -0.2), width=0.3, height=0.2, color="green", action=self.replay))
        self.add_element(ButtonElement(win, "Quit", pos=(0, -0.5), width=0.3, height=0.2, color="red", action=self.quit))

    def replay(self):
        return StartScreen(self.win)

    def quit(self):
        return None  # This will end the experiment

# StartScreen
class StartScreen(BaseScreen):
    def __init__(self, win):
        super().__init__(win)
        self.add_element(TextElement(win, "Quizz Experiment", pos=(0, 0),color=color_dict["black"]))
        self.add_element(ButtonElement(win, "Start", pos=(0, -0.2), width=0.3, height=0.2, color="green", action=self.next_screen))

    def next_screen(self):
        return TestScreen(self.win)

# TestScreen
class TestScreen(BaseScreen):
    def __init__(self, win):
        super().__init__(win)
        self.answerList  = self.get_m4a_files(audio_dir)
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

        
    def next_question(self):
        self.current_index += 1
        self.update_button_states()
        self.updateProcess()
        return self
    
    def previous_question(self):
        self.current_index -= 1
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
        
        current_question = self.answerList[self.current_index]
        self.bofomo_consonants_list.updateState(current_question.get_answer())
        self.similarities_list.updateState(current_question.get_similarity())

    def submit_test(self):
        return EndScreen(self.win)
    
    def updateProcess(self):
        self.progress.set_text("Test Number:{}/{}".format(self.current_index+1,len(self.answerList)))
    
    # Action for BofoMo consonants
    def bofomo_consonant_action(self, button_index):
        # This function is called when a BofoMo consonant button is clicked.
        # 'button_index' is the index of the button that was clicked.
        selected_consonant = pofomopo_consonants[button_index]
        current_question = self.answerList[self.current_index]
        current_question.set_answer(button_index)
        print(f"BofoMo consonant button clicked: {selected_consonant}")
        self.bofomo_consonants_list.updateState(current_question.get_answer())
        return self

    # Action for similarities
    def similarity_action(self, button_index):
        # This function is called when a similarity button is clicked.
        # 'button_index' is the index of the button that was clicked.
        selected_similarity = similarity_list[button_index]
        current_question = self.answerList[self.current_index]
        current_question.set_similarity(button_index)
        print(f"Similarity button clicked: {selected_similarity}")
        self.similarities_list.updateState(current_question.get_similarity())
        return self