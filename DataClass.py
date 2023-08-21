import pickle
import numpy as np
import pandas as pd
import re

class DataClass():
    def __init__(self):
        print("__init__ is called\n")


    def get_data(self, height, weight, fit, gender, temp):
        self.height = height
        self.weight = weight
        self.fit = fit
        self.gender = gender
        self.temp = temp


    def print_data(self):
        print(self.height)
        print(self.weight)
        print(self.fit)
        print(self.gender)
        print(self.temp)


    def return_data(self):
        dataFrame = self.toDataFrame()
        # pickle 가져오기
        model = self.get_random_forest_model()
        scale = self.get_standard_scaler_object()
        ohe = self.get_one_hot_encoder_object()
        
        # 데이터 전처리
        scale_result = scale.transform(dataFrame[['height(cm)', 'weight(kg)', 'temp']])
        ohe_result = ohe.transform(dataFrame[['gender', 'fit']])

        # 배열로 변환
        X_user = pd.concat([pd.DataFrame(scale_result), pd.DataFrame(ohe_result.toarray())], axis=1)

        # 예측값 가져오기
        prediction = model.predict(X_user)
        prediction_result = prediction[0]
        print(prediction_result)

        pattern_size = r'[SMLX]{1,3}'
        pattern_num = r'\d{1,2}'

        result_size = re.search(pattern_size, prediction_result).group() # size 
        result_num = re.search(pattern_num, prediction_result).group() # number

        return (result_size, result_num)
    
    # standard scaler 파일 가져오기
    def get_standard_scaler_object(self):
        scale = ''
        with open('standard_scaler.pickle', 'rb') as f:
            scale = pickle.load(f)

        return scale
    
    # one hot encoder 파일 가져오기
    def get_one_hot_encoder_object(self):
        ohe = ''
        with open('one_hot_encoder.pickle', 'rb') as f:
            ohe = pickle.load(f)

        return ohe

    # random forest 파일 가져오기
    def get_random_forest_model(self):
        random_forest = ''
        with open('rf.pickle', 'rb') as f:
            random_forest = pickle.load(f)

        return random_forest
    

    def toDataFrame(self):
        dataObject = {
            "height(cm)" : self.height,
            "weight(kg)" : self.weight,
            "fit" : self.fit,
            "gender" : self.gender,
            "temp" : self.temp
        }

        dataFrame = pd.DataFrame(dataObject, index=[0])
        return dataFrame
    
    def toValue(self):
        dataObject = {
            "height(cm)" : self.height,
            "weight(kg)" : self.weight,
            "fit" : self.fit,
            "gender" : self.gender,
            "temp" : self.temp
        }
        return dataObject
    
    def find_image_link(self, result_num):
        df = pd.read_csv('unique_c_image_data.csv')
        result_num = int(result_num)
        matching_row = df[df['number']==result_num]
        image_link = matching_row['image_link'].values[0]

        if not matching_row.empty: 
            return image_link
        else:
            return "No matching image link found"
    
    
    def find_purchase_link(self, result_num):
        df = pd.read_csv('unique_c_image_data.csv')
        result_num = int(result_num)
        matching_row = df[df['number']==result_num]
        purchase_link = matching_row['purchase'].values[0]
        print(purchase_link)
        
        if not matching_row.empty:
            return purchase_link
        else:
            return "No matching purchase link found"