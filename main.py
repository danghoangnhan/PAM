from component.screen import StartScreen
import logging
from PyQt6.QtWidgets import QApplication
import logging


class Game:
    def __init__(self):
        self.screen_height = 1200  
        self.screen_width = 800  
        pass
    def start(self):
        app = QApplication([])
        start_screen = StartScreen(self.screen_height,self.screen_width)
        start_screen.show()
        app.exec()

if __name__ == "__main__":
    try:
        game = Game()
        game.start()
    except Exception as e:
        logging.error("An error occurred: %s", str(e))