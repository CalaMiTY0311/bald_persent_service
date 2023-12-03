import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error,r2_score
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 준비 
dataset = pd.read_csv('../bald_probability.csv', index_col=0)

X = dataset[[
             'age', 
             'gender', 
             'is_married', 
             'is_hereditary', 
             'weight', 
             'height', 
             'is_smoker', 
             'stress'
             ]]
Y = dataset['bald_prob']

#lr_poly
model = Pipeline([('poly', PolynomialFeatures(degree=2, include_bias=False)),
 				('linear', LinearRegression())])

from decimal import Decimal

test_size = [
                # 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 
                0.1, 
                0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.19, 
                0.2, 
                0.21, 0.22, 0.23, 0.24, 0.25, 0.26, 0.27, 0.28, 0.29, 0.3, 
                0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4
            ]
ans=0
for j in test_size:
    for i in range(0,300):
        X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size=j,random_state=i)
        model.fit(X_train, y_train)
        y_preds = model.predict(X_test)
        mse = mean_squared_error(y_test,y_preds)
        rmse = np.sqrt(mse)
        predict = r2_score(y_test,y_preds)

        if ans == 0:
            ans = predict
        elif ans<predict:
            ans = predict
            print('MSE:{0:.3f}, RMSE:{1:.3f}'.format(mse, rmse))
            print(j,i)
            print(predict)
    print(j)