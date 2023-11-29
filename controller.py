from PyQt6.QtWidgets import QApplication
import sys
import logging
from component.screen import StartScreen,TestScreen,UserInformationScreen,EndScreen,SettingScreen

class Navigator:
    def __init__(self,screen_height:int =1200,screen_width:int = 800):
        self.app = QApplication(sys.argv)
        self.screen_height = screen_height  
        self.screen_width = screen_width
        
        self.start_screen = StartScreen(navigator=self,screen_height=self.screen_height,screen_width=self.screen_width)
        self.setting_screen = SettingScreen(navigator=self,screen_height=self.screen_height,screen_width=self.screen_width)
        self.user_info_screen = UserInformationScreen(navigator=self,screen_height=self.screen_height,screen_width=self.screen_width)
        self.end_screen = EndScreen(navigator=self,screen_height=self.screen_height,screen_width=self.screen_width,result=None)
        self.test_screen = TestScreen(navigator=self,screen_height=self.screen_height,screen_width=self.screen_width)

    def start(self):
        self.start_screen.show()
        sys.exit(self.app.exec())

    def navigate_to_setting_screen(self):
        logging.info(" Open the settings screen")
        self.close_all()
        self.setting_screen.show()
        

    def navigate_to_start_screen(self):
        self.close_all()
        self.start_screen.show()

    def navigate_to_user_info_screen(self):
        logging.info("Open the user information screen")
        self.close_all()
        self.user_info_screen.show()

        self.user_info_screen.show()

    def navigate_to_end_screen(self):
        logging.info("Open the user end screen")
        self.close_all()
        self.end_screen.show()  
    
    def navigate_to_test_screen(self):
        logging.info("Open the test screen")
        self.close_all()
        self.test_screen.show()    
    
    def close_all(self):
        logging.info("close all")
        self.test_screen.close()    
        self.end_screen.close()  
        self.user_info_screen.close()
        self.start_screen.close()
        self.setting_screen.close()        
