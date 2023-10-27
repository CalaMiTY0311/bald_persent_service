import numpy as np
import pandas as pd
from sklearn import datasets
#
from sklearn import model_selection
from sklearn.svm import SVR
from sklearn import metrics
import os

directory = os.path.dirname(__file__)
path = os.path.join(directory, 'bald_probability.csv')

dataset = pd.read_csv(path, index_col=0, encoding='utf-8-sig')


x_data = dataset[['age', 'gender', 'is_married', 'is_hereditary', 'weight', 'height', 'is_smoker', 'stress']]
y_data = dataset['bald_prob']
#print(x_data.shape) #(20640, 8)
#print(y_data.shape) #(20640,)

####################

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(x_data)
x_data = scaler.transform(x_data)

x_train, x_test, y_train, y_test = model_selection.train_test_split(x_data, y_data, test_size=0.3)


def svm_score():
    estimator = SVR(kernel='rbf', C=1.0, gamma='auto')

    estimator.fit(x_train, y_train)

    y_predict = estimator.predict(x_train) 
    svm_score_train = metrics.r2_score(y_train, y_predict)

    y_predict = estimator.predict(x_test) 
    svm_score_test = metrics.r2_score(y_test, y_predict)

    print("svm_score_train : ", svm_score_train)
    print("svm_score_test : ", svm_score_test)