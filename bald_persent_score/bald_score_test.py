import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error,r2_score
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 준비 
dataset = pd.read_csv('bald_probability.csv', index_col=0)

X = dataset[['age', 
             'gender', 
             'is_married', 
             'is_hereditary', 
             'weight', 
             'height', 
             'is_smoker', 
             'stress'
             ]]
Y = dataset['bald_prob']

X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size=0.3,random_state=156)

model = Pipeline([('poly', PolynomialFeatures(degree=2, include_bias=False)),
 				('linear', LinearRegression())])

model.fit(X_train, y_train)
y_preds = model.predict(X_test)
mse = mean_squared_error(y_test,y_preds)
rmse = np.sqrt(mse)

print('MSE:{0:.3f}, RMSE:{1:.3f}'.format(mse, rmse))
print('Variance score:{0:.3f}'.format(r2_score(y_test, y_preds)))