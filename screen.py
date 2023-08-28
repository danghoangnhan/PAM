from button import ButtonElement
from text import TextElement


class Screen:
    def __init__(self, win):
        self.win = win
        self.elements = []

    def add_element(self, element):
        self.elements.append(element)

    def draw(self):
        for element in self.elements:
            element.draw()

# Define your screens as classes
class StartScreen(Screen):
    def __init__(self, win):
        super().__init__(win)
        start_button = visual.Rect(win, width=0.2, height=0.1, fillColor="green", pos=(0, -0.2))
        self.add_element(TextElement(win, "Test Name", pos=(0, 0)))
        self.add_element(ButtonElement(win, "Start", pos=(0, -0.2), width=0.2, height=0.1, color="green", action=self.next_screen))

    def next_screen(self):
        return AudioListScreen(self.win)

class AudioListScreen(Screen):
    def __init__(self, win):
        super().__init__(win)
        self.add_element(TextElement(win, "Audio List", pos=(0, 0)))
        # Add audio stimuli and answer buttons here
        # Example:
        # self.add_element(ButtonElement(win, "Play Sound", pos=(-0.4, 0.2), width=0.2, height=0.1, color="blue", action=self.play_sound))

    def play_sound(self):
        # Add logic to play audio here
        pass