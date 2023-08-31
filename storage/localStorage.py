import pandas
from config.dir import user_dir,history_dir,exam_dir

class csvHandler:
        
    @staticmethod
    def get_new_sessionId():
        user_df = pandas.read_csv(user_dir)
        max_value = user_df['participantID'].max()
        return max_value+1
    
    @staticmethod
    def get_new_sessionId():
        user_df = pandas.read_csv(user_dir)
        max_value = user_df['participantID'].max()
        return max_value+1
    
    @staticmethod
    def get_exam():
        return pandas.read_csv(exam_dir)
    
    @staticmethod
    def append_history_data(new_df):
        csvHandler.append_data(new_df,history_dir)

    @staticmethod
    def append_data(new_df,csv_file_path):
        new_df.to_csv(csv_file_path, mode='a', header=False, index=False)

    @staticmethod
    def dumpd_data():
        history_df = pandas.read_csv(history_dir)
        history_dir.to_excel('history.xlsx', index=False)
