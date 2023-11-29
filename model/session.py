
class Session:
    def __init__(self):
        self.user_info = None
        
    def set_user_info(self, info:dict):
        self.user_info = info

    def get_user_info(self)->dict:
        return self.user_info
    
currentSession = Session()