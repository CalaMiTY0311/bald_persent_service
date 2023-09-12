import numpy as np
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import pandas as pd
import os

# 데이터 준비
#options = dataset[['age', 'gender', 'is_married', 'is_hereditary', 'weight', 'height', 'is_smoker', 'stress']]
#bald_prob = dataset['bald_prob']

#X_train, X_test, y_train, y_test = train_test_split(options, 
#                                                    bald_prob, 
#                                                    test_size = 0.3,
#                                                    random_state=156)

directory = os.path.dirname(__file__)
path = os.path.join(directory, 'bald_probability.csv')

dataset = pd.read_csv(path, index_col=0, encoding='utf-8-sig')

train, test = train_test_split(dataset, test_size = 0.3)
X_train = train[['age', 'gender', 'is_married', 'is_hereditary', 'weight', 'height', 'is_smoker', 'stress']]
y_train = train['bald_prob']
X_test = test[['age', 'gender', 'is_married', 'is_hereditary', 'weight', 'height', 'is_smoker', 'stress']] 
y_test = test['bald_prob']

poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

model = LinearRegression()
complete_model = model.fit(X_train_poly, y_train)

def accuracy_result():
#----------------------------------------------------accuracy----------------------------------------------------
	y_pred = complete_model.predict(X_test_poly)
	# 잔차 구하기 

	y_mean = np.mean(y_test) 
	# # y 평균값 # $\sum(y 예측값 - y 평균값)^2$ = 예측값에 대한 편차 
	nomerator = np.sum(np.square(y_test - y_pred)) # $sum(y 관측값 - y 평균값)^2$ 
	denominator = np.sum(np.square(y_test - y_mean)) 
	accuracy = 1 - nomerator / denominator 
	return accuracy
#----------------------------------------------------accuracy----------------------------------------------------

def predict_result(data):
	data = poly.transform(data)
	predict = complete_model.predict(data)
	return predict

# # 그래프 그리기
# plt.figure(figsize=(8, 6))

# # 실제값과 예측값의 산점도 그리기
# plt.scatter(y_test, y_pred, color='blue', alpha=0.7)
# plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linewidth=2)  # 대각선 기준선

# plt.title("실제값 대 예측값")
# plt.xlabel("실제값")
# plt.ylabel("예측값")
# plt.show()