from psychopy import visual

class TextElement:
    def __init__(self, win, text, pos):
        self.text = visual.TextStim(win, text=text, pos=pos)

    def draw(self):
        self.text.draw()