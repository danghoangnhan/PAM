from psychopy import visual
from component.text import TextElement


class ButtonElement:
    def __init__(self, win, text, pos, width, height, color, action=None):
        self.button = visual.Rect(win, width=width, height=height, fillColor=color, pos=pos)
        

        self.text = TextElement(win=win,text=text,pos=pos)

        self.action = action
        self.states = {
                        'unpress': {
                            'button_color': 'navy',
                            'text_color': 'white'
                        },
                        'press': {
                            'button_color': 'orange',
                            'text_color': 'black'
                        }
                    }        
        self.state = 'unpress'  # Initial state is 'unpress'
        # self.button = visual.ImageStim(
        #     win=win,
        #     image=self.text.create_text_image(width=width,height=height),
        #     pos=pos,
        #     size=(width, height)
        # )   

    def draw(self):
        self.button.fillColor = self.states[self.state]['button_color']
        self.text.set_color(self.states[self.state]['text_color'])
        self.button.draw()
        self.text.draw()

    def containMouse(self,mouse):
        return self.button.contains(mouse)
        

class ButtonList:
    def __init__(self, win, textList, pos, width, height, color, action=None,rows=0,columns=0,horizontal_spacing=0,vertical_spacing=0):
        self.pos = pos
        positions = []
        for row in range(rows):
            for col in range(columns):
                x = col * (width + horizontal_spacing) - (columns - 1) * (width + horizontal_spacing) / 2
                y = (rows - 1 - row) * (height + vertical_spacing) - (rows - 1) * (height + vertical_spacing) / 2
                positions.append((x, y))

        self.button_elements = []
        for i, text in enumerate(textList):
            button_pos = (positions[i][0] + self.pos[0], positions[i][1] + self.pos[1])  # Use positions[i] here
            self.button_elements.append(ButtonElement(win, text, pos=button_pos, width=width, height=height, color=color, action=action))

    def draw(self):
        for element in self.button_elements:
            element.draw()

    def containMouse(self, mouse):
        return any(element.containMouse(mouse) for element in self.button_elements)

    
    def action(self,mouse):
        for element_id,element in enumerate(self.button_elements):
            if element.containMouse(mouse):
                return element.action(element_id)
            
    def updateState(self,buttonId):
        for element_id,element in enumerate(self.button_elements):
            element.state = 'unpress'
            if element_id==buttonId:
                element.state = 'press'

