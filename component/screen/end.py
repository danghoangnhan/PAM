# EndScreen
from component.button import ButtonElement
from component.screen.base import BaseScreen
from component.screen.start import StartScreen
from component.text import TextElement


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