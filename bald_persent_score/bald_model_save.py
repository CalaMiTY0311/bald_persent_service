import numpy as np
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import pandas as pd
import os

directory = os.path.dirname(__file__)
path = os.path.join(directory, 'bald_probability.csv')

dataset = pd.read_csv(path, index_col=0, encoding='utf-8-sig')

train, test = train_test_split(dataset, test_size = 0.11, random_state = 42)
X_train = train[['age', 'gender', 'is_married', 'is_hereditary', 'weight', 'height', 'is_smoker', 'stress']]
y_train = train['bald_prob']
X_test = test[['age', 'gender', 'is_married', 'is_hereditary', 'weight', 'height', 'is_smoker', 'stress']] 
y_test = test['bald_prob']

poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

model = LinearRegression()
complete_model = model.fit(X_train_poly, y_train)

import joblib

# model save
joblib.dump(complete_model, 'complete_model.pkl')
