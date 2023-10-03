from component.button import ButtonElement, ButtonList
from psychopy import visual, core, event
from component.screen import StartScreen
import logging
import psychopy.visual.line

from mouseHandler import is_instance_of_class



class Game:
    def __init__(self):
        self.win  = visual.Window([1200, 800], color="white")
        self.current_screen = StartScreen(self.win)
        self.mouse = event.Mouse()

    def start(self):
        while self.current_screen is not None:
                self.current_screen.draw()
                self.win.flip()

                # Check for mouse clicks
                if self.mouse.getPressed()[0]:  # 0 represents the left mouse button
                    for element in self.current_screen.elements:
                        if is_instance_of_class(element) and  element.containMouse(self.mouse):
                            if element.action:
                                self.setScreen(element.action(self.mouse))
                                core.wait(0.2)
        print("screen is None")
        self.win.close()
        core.quit()

    def setScreen(self,screen):
        self.current_screen = screen
try:
    game = Game()
    game.start()
except Exception as e:
    logging.error("An error occurred: %s", str(e))




