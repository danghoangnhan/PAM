from psychopy import visual

class ButtonElement:
    def __init__(self, win, text, pos, width, height, color, action=None):
        self.button = visual.Rect(win, width=width, height=height, fillColor=color, pos=pos)
        self.text = visual.TextStim(win, text=text, pos=pos)
        self.action = action

    def draw(self):
        self.button.draw()
        self.text.draw()
