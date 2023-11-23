import numpy as np
import pandas as pd
#
from sklearn.preprocessing import PolynomialFeatures
from sklearn import model_selection
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import os

directory = os.path.dirname(__file__)
path = os.path.join(directory, 'bald_probability.csv')

dataset = pd.read_csv(path, index_col=0, encoding='utf-8-sig')


x_data = dataset[['age', 'gender', 'is_married', 'is_hereditary', 'weight', 'height', 'is_smoker', 'stress']]
y_data = dataset['bald_prob']
#print(x_data.shape) #(506, 13)
#print(y_data.shape) #(506,)

x_train, x_test, y_train, y_test = model_selection.train_test_split(x_data, y_data, test_size=0.3)

def lr_score():

    global x_train, x_test, y_train, y_test

    estimator = LinearRegression()

    estimator.fit(x_train, y_train)

    y_predict = estimator.predict(x_train) 
    lr_score_train = metrics.r2_score(y_train, y_predict)
    #print(score) #1.0

    y_predict = estimator.predict(x_test) 
    lr_score_test = metrics.r2_score(y_test, y_predict)
    #print(score) #1.0
    print("lr_score_train : ",lr_score_train)
    print("lr_score_test : ",lr_score_test)
    print()
    print()

    poly = PolynomialFeatures(degree=2, include_bias=False)
    poly.fit(x_data)
    x_data_poly = poly.transform(x_data)

    x_train, x_test, y_train, y_test = model_selection.train_test_split(x_data_poly, y_data, test_size=0.3)

    estimator = LinearRegression()

    estimator.fit(x_train, y_train)

    y_predict = estimator.predict(x_train) 
    lr_poly_score_train = metrics.r2_score(y_train, y_predict)
    #print(score) #1.0

    y_predict = estimator.predict(x_test) 
    lr_poly_score_test = metrics.r2_score(y_test, y_predict)
    
    print("lr_poly_score_train : ",lr_poly_score_train)
    print("lr_poly_score_test : ",lr_poly_score_test)
    print()
    print()



