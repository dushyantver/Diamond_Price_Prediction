import os
import sys
import pandas as pd
from src.exception.exception import customexception
from src.logger.logger import logging
from src.utils.utility import load_object


class PredictPipeline:

    def __init__(self):
        print("init.. the object")

    def predict(self,features):
        try:
            preprocessor_path=os.path.join("artifacts","preprocessor.pkl")
            model_path=os.path.join("artifacts","model.pkl")

            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)

            scaled_fea=preprocessor.transform(features)
            pred=model.predict(scaled_fea)

            return pred

        except Exception as e:
            raise customexception(e,sys)

class CustomData:
    def __init__(self,
                 Carat:float,
                 Depth:float,
                 Table:float,
                 x:float,
                 y:float,
                 z:float,
                 Cut:str,
                 Color:str,
                 Clarity:str):
        
        self.Carat=Carat
        self.Depth=Depth
        self.Table=Table
        self.x=x
        self.y=y
        self.z=z
        self.Cut = Cut
        self.Color = Color
        self.Clarity = Clarity
            
    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'carat':[self.Carat],
                'depth':[self.Depth],
                'table':[self.Table],
                'x':[self.x],
                'y':[self.y],
                'z':[self.z],
                'cut':[self.Cut],
                'color':[self.Color],
                'clarity':[self.Clarity]
                }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('Dataframe Gathered')
            return df
        except Exception as e:
            logging.info('Exception Occured in prediction pipeline')
            raise customexception(e,sys)