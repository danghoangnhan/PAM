from psychopy import visual

class ButtonElement:
    def __init__(self, win, text, pos, width, height, color, action=None):
        self.button = visual.Rect(win, width=width, height=height, fillColor=color, pos=pos)
        self.text = visual.TextStim(win, text=text, pos=pos)
        self.action = action

    def draw(self):
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

            print(button_pos)
            self.button_elements.append(ButtonElement(win, text, pos=button_pos, width=width, height=height, color=color, action=action))

    def draw(self):
        for element in self.button_elements:
            element.draw()

    def containMouse(self, mouse):
        return any(element.containMouse(mouse) for element in self.button_elements)

    
    def action(self,mouse):
        for element_id,element in enumerate(self.button_elements):
            if element.containMouse(mouse):
                element.action(element_id)

