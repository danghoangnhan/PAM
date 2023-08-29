from component.button import ButtonElement
from component.screen.base import BaseScreen
from component.screen.test import TestScreen
from component.text import TextElement

# StartScreen
class StartScreen(BaseScreen):
    def __init__(self, win):
        super().__init__(win)
        self.add_element(TextElement(win, "Test Name", pos=(0, 0)))
        self.add_element(ButtonElement(win, "Start", pos=(0, -0.2), width=0.2, height=0.1, color="green", action=self.next_screen))

    def next_screen(self):
        return TestScreen(self.win)