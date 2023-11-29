import os
import pandas
from config.dir import user_dir,history_dir,exam_dir,metadata_dir,keyboard_dir
import json

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


class JsonHandler:
    def __init__(self, dir):
        self.dir = dir

    def read_data(self):
        try:
            with open(self.dir, 'r') as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            return None

    def write_data(self, data):
        with open(self.dir, 'w') as file:
            json.dump(data, file, indent=4)

    def append_data(self, new_data):
        existing_data = self.read_data()
        if existing_data is None:
            existing_data = []
        existing_data.extend(new_data)
        self.write_data(existing_data)



class DataHandaler:
    def __init__(self):

        self.user_data_handaler =xlsxHandler(dir=user_dir)
        self.history_data_handaler =xlsxHandler(dir=history_dir)
        self.exam_data_handler = xlsxHandler(dir=exam_dir)
        self.metadata_handler = JsonHandler(dir=metadata_dir)

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
    
    def loadMetaData(self):
        return self.metadata_handler.read_data(metadata_dir)
    
    def saveMetaData(self,data_dict):
        self.metadata_handler.write_data(data_dict)
    
    def getKeyboardList(self):
        setting_dict = self.metadata_handler.read_data()
        tmp_excel_handler = xlsxHandler(dir = os.path.join(keyboard_dir,setting_dict['selected_keyboard_layout']))
        df = tmp_excel_handler.readData()
        return df['label'].to_list()
    
    def getSimilarities(self):
        setting_dict = self.metadata_handler.read_data()       
        return  list(range(1, int( setting_dict['selected_similarity']) + 1))

dataHandaler= DataHandaler()