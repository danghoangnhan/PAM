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
        exam_dir = pandas.read_csv(exam_dir)
        return exam_dir
    
    @staticmethod
    def append_data(new_df,csv_file_path):
        new_df.to_csv(csv_file_path, mode='a', header=False, index=False)

    @staticmethod
    def dumpd_data():
        user_df = pandas.read_csv(user_dir)
        exam_df = pandas.read_csv(exam_dir)
        history_df = pandas.read_csv(history_dir)
        
        user_df.to_excel('user_df.xlsx', index=False)
        exam_dir.to_excel('exam_df.xlsx', index=False)
        history_dir.to_excel('history_df.xlsx', index=False)
