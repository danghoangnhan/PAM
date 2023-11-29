import pandas
from config.dir import user_dir,history_dir,exam_dir

class xlsxHandler:
    
    def __init__(self,dir):
        self.dir = dir
    
    def readData(self):
        return pandas.read_excel(self.dir)
    
    def readStructure(self):
        return  pandas.read_excel(self.dir, nrows=1)
    
    def dumpd_data(self):
        history_dir.to_excel(self.dir, index=False)
    
    def truncate(self):
            df = pandas.read_excel(self.dir)
            df = pandas.DataFrame(columns=df.columns)
            df.to_excel(self.dir, index=False)

    def append_data(self,new_df):
            df_excel = pandas.read_excel(self.dir)
            result = pandas.concat([df_excel, new_df], ignore_index=True)
            print(result)
            result.to_excel(self.dir, index=False)
    

class DataHandaler:
    def __init__(self):

        self.user_data_handaler =xlsxHandler(dir=user_dir)
        self.history_data_handaler =xlsxHandler(dir=history_dir)
        self.exam_data_handler = xlsxHandler(dir=exam_dir)

    def get_new_sessionId(self):
        user_df =  self.user_data_handaler.readData()
        if user_df.empty:
            return 1
        max_value = user_df['participantID'].max()
        return int(max_value) + 1
    
    def get_exam(self):
        return pandas.read_excel(exam_dir)
    
    def get_user(self):
        return self.user_data_handaler.readData()
    
    def append_history_data(self,new_df):
        self.history_data_handaler.append_data(new_df=new_df)

    def append_user_data(self,new_df):
        self.user_data_handaler.append_data(new_df=new_df)
        
    def readStructure_user(self):
        return  self.user_data_handaler.readStructure()
    
    def resetHistory(self):
        self.user_data_handaler.truncate()
        self.history_data_handaler.truncate()

dataHandaler= DataHandaler()