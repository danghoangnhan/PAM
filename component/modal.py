from component.text import TextElement
from component.button import ButtonElement
import psychopy.visual.line
from psychopy.visual.rect import Rect
from config.constant import color_dict

class ConfirmationModal:
    def __init__(self, win, text,confirm_action=None,cancel_action=None):
        self.win = win
        self.text = TextElement(win, text, pos=(0, 0), color=color_dict["white"],)
        self.confirm_button = ButtonElement(win, "Confirm", pos=(-0.3, -0.5), width=0.3, height=0.2, color="green", action=confirm_action)
        self.cancel_button = ButtonElement(win, "Cancel", pos=(0.3, -0.5), width=0.3, height=0.2, color="red", action=cancel_action)
        self.background_rect = Rect(win, width=1.2, height=0.9, fillColor=(0, 0, 0, 1.0), pos=(0, -0.2))
        self.buttons =  [self.confirm_button, self.cancel_button]
        self.visible = False

    def draw(self):
        if self.visible:
            self.background_rect.draw()
            self.text.draw()
            for element in self.buttons:
                element.draw()

    def containMouse(self, mouse):
        if(self.visible)==False:
            return False
        return self.confirm_button.containMouse(mouse) or self.cancel_button.containMouse(mouse)

    def action(self, mouse):
            for button_element in self.buttons:
                if button_element.containMouse(mouse):
                    return button_element.action(mouse)