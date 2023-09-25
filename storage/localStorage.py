import pandas
from config.dir import user_dir,history_dir,exam_dir

class csvHandler:
        
    @staticmethod
    def get_new_sessionId():
        user_df = pandas.read_excel(user_dir)
        if user_df.empty:
            return 1
        max_value = user_df['participantID'].max()
        return int(max_value) + 1
    
    @staticmethod
    def get_exam():
        return pandas.read_excel(exam_dir)
    
    @staticmethod
    def get_user():
        return pandas.read_excel(user_dir)
    
    @staticmethod
    def append_history_data(new_df):
        csvHandler.append_data(new_df,history_dir)
        
    @staticmethod
    def append_user_data(new_df):
        csvHandler.append_data(new_df,user_dir)

    @staticmethod
    def append_data(new_df,path):
        new_df.to_excel(path, index=False)


    @staticmethod
    def dumpd_data():
        history_df = pandas.read_excel(history_dir)
        history_dir.to_excel('history.xlsx', index=False)
    
    @staticmethod
    def readStructure_user():
        return  csvHandler.readStructure(user_dir)

    @staticmethod
    def readStructure(dir):
        return  pandas.read_excel(dir, nrows=1)
