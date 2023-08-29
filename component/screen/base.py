class BaseScreen:
    def __init__(self, win):
        self.win = win
        self.elements = []

    def add_element(self, element):
        self.elements.append(element)

    def draw(self):
        for element in self.elements:
            element.draw()