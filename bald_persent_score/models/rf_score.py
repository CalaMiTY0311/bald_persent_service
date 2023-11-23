import numpy as np
import pandas as pd
#
from sklearn.preprocessing import PolynomialFeatures
from sklearn import model_selection
from sklearn.ensemble import RandomForestRegressor
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

def rf_score():

    global x_train, x_test, y_train, y_test

    from sklearn.ensemble import RandomForestRegressor
    estimator = RandomForestRegressor()

    estimator.fit(x_train, y_train)

    y_predict = estimator.predict(x_train) 
    rf_score_train = metrics.r2_score(y_train, y_predict)

    y_predict = estimator.predict(x_test) 
    rf_score_test = metrics.r2_score(y_test, y_predict)
    print("rf_score_train : ",rf_score_train) #1.0
    print("rf_score_test : ",rf_score_test) #1.0
    print()
    print()

    poly = PolynomialFeatures(degree=3)
    poly.fit(x_data)
    x_data_poly = poly.transform(x_data)

    x_train, x_test, y_train, y_test = model_selection.train_test_split(x_data_poly, y_data, test_size=0.2)

    estimator = RandomForestRegressor()

    estimator.fit(x_train, y_train)

    y_predict = estimator.predict(x_train) 
    rf_poly_score_train = metrics.r2_score(y_train, y_predict)

    y_predict = estimator.predict(x_test) 
    rf_poly_score_test = metrics.r2_score(y_test, y_predict)

    print("rf_poly_score_train : ", rf_poly_score_train) #1.0
    print("rf_poly_score_test : ", rf_poly_score_test) #1.0
    print()
    print()