from psychopy.visual import TextStim
from config.dir import font_dir


class TextElement:
    def __init__(self, win, text, pos, color=(1, 1, 1)):
        self.text = TextStim(win, text=text, pos=pos, color=color,colorSpace='rgb',font='Noto Sans TC',fontFiles=[font_dir])
    def set_text(self,text):
        self.text.setText(text)
    def set_color(self,color):
        self.text.setColor(color=color)
    def draw(self):
        self.text.draw()