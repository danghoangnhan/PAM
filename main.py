from component.button import ButtonElement, ButtonList
from psychopy import visual, core, event
from component.screen import StartScreen


class Game:
    def __init__(self):
        self.win  = visual.Window([800, 600], color="white")
        self.current_screen = StartScreen(self.win)
        self.mouse = event.Mouse()
    def start(self):
        while self.current_screen is not None:
                self.current_screen.draw()
                self.win.flip()

                # Check for mouse clicks
                if self.mouse.getPressed()[0]:  # 0 represents the left mouse button
                    for element in self.current_screen.elements:
                        if isinstance(element, ButtonElement) and element.containMouse(self.mouse):
                            if element.action:
                                self.setScreen(element.action())
                                core.wait(0.2)
                        if isinstance(element, ButtonList) and element.containMouse(self.mouse):
                            if element.action:
                                self.setScreen(element.action(mouse=self.mouse))
                                core.wait(0.2)
        if self.current_screen==None:
            print("screen is none")
        self.win.close()
        core.quit()

    def setScreen(self,screen):
        self.current_screen = screen

game = Game()
game.start()





