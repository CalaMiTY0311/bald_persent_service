import numpy as np
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import pandas as pd
import os
import joblib

directory = os.path.dirname(__file__)

model = joblib.load('complete_model.pkl')

data = np.array([24, 1, 0, 1, 83, 175, 0, 7]).reshape(1, -1)
poly = PolynomialFeatures(degree=2)
data = poly.fit_transform(data)

predict = model.predict(data)
print(predict)
