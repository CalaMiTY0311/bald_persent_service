import pandas as pd
import os
import csv

# directory = os.path.dirname(__file__)
# path = os.path.join(directory, 'bald_probability.csv')

# dataset = pd.read_csv(path, index_col=0, encoding='utf-8-sig')

#dataset = pd.read_csv('bald_probability.csv',index_col = 0,encoding='utf-8-sig')

#dataset = dataset.dropna()                                                     #NAN/빈값있는 행 제거

#dataset.drop(['job_role','province','salary','shampoo','education'],axis = 1,inplace =True)             #행 제거 
#age,gender,job_role,province,salary,is_married,is_hereditary,weight,height,shampoo,is_smoker,education,stress,bald_prob

#dataset = dataset.astype({'gender':'string'})                    #행 타입 변경

#dataset['gender'] = dataset['gender'].map({'male': 1, 'female': 0})            #dataset에 gender를 정수로 변경 남자=1 여자=0

#dataset = dataset.astype({'is_smoker':'int','stress':'int','age':'int'})                    #행 타입 변경

#dataset['bald_prob'] = dataset['bald_prob'].apply(lambda x: int(x * 1000) / 1000)             #float형태의 행을 전부 첫째 점까지 반올림하는 코드

#dataset.drop(dataset['index'], axis=1, inplace=True)

#dataset.insert(0,'index',0)
#dataset.to_csv('bald_probability.csv')
#print(dataset.columns)

