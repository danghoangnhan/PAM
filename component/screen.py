from component.button import ButtonElement
from component.text import TextElement
from config.font import color_dict

class Screen:
    def __init__(self, win):
        self.win = win
        self.elements = []

    def add_element(self, element):
        self.elements.append(element)

    def draw(self):
        for element in self.elements:
            element.draw()


# StartScreen
class StartScreen(Screen):
    def __init__(self, win):
        super().__init__(win)
        self.add_element(TextElement(win, "Test Name", pos=(0, 0)))
        self.add_element(ButtonElement(win, "Start", pos=(0, -0.2), width=0.2, height=0.1, color="green", action=self.next_screen))

    def next_screen(self):
        return TestScreen(self.win)

# TestScreen
class TestScreen(Screen):
    def __init__(self, win):
        super().__init__(win)
        self.add_element(TextElement(win, "Audio Test List", pos=(0, 0)))
        # Add audio stimuli and answer buttons here
        # Example:
        self.add_element(ButtonElement(win, "Play Sound", pos=(-0.4, 0.2), width=0.2, height=0.1, color="blue", action=self.play_sound))

    def play_sound(self):
        # Add logic to play audio here
        pass

# EndScreen
class EndScreen(Screen):
    def __init__(self, win):
        super().__init__(win)
        self.add_element(TextElement(win, "Thank you for participating!", pos=(0, 0)))
        self.add_element(ButtonElement(win, "Replay", pos=(0, -0.2), width=0.2, height=0.1, color="green", action=self.replay))
        self.add_element(ButtonElement(win, "Quit", pos=(0, -0.4), width=0.2, height=0.1, color="red", action=self.quit))

    def replay(self):
        return StartScreen(self.win)

    def quit(self):
        return None  # This will end the experiment