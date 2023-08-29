from psychopy import visual

class TextElement:
    def __init__(self, win, text, pos, color=(1, 1, 1)):
        self.text = visual.TextStim(win, text=text, pos=pos, color=color,colorSpace='rgb')
    def set_text(self,text):
        self.text.text = text
        
    def draw(self):
        self.text.draw()
