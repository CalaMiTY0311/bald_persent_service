import numpy as np
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from bald_csv_edit import dataset
import matplotlib.pyplot as plt
import pandas as pd


# 데이터 준비
#options = dataset[['age', 'gender', 'is_married', 'is_hereditary', 'weight', 'height', 'is_smoker', 'stress']]
#bald_prob = dataset['bald_prob']

#X_train, X_test, y_train, y_test = train_test_split(options, 
#                                                    bald_prob, 
#                                                    test_size = 0.3,
#                                                    random_state=156)

train, test = train_test_split(dataset, test_size = 0.3)
X_train = train[['age', 'gender', 'is_married', 'is_hereditary', 'weight', 'height', 'is_smoker', 'stress']]
y_train = train['bald_prob']
X_test = test[['age', 'gender', 'is_married', 'is_hereditary', 'weight', 'height', 'is_smoker', 'stress']] 
y_test = test['bald_prob']

poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

model = LinearRegression()
model.fit(X_train_poly, y_train)
complete_model = model
y_pred = model.predict(X_test_poly)

new_data = np.array([24, 1, 0, 1, 83, 175, 0, 7]).reshape(1, -1)  # reshape를 통해 2D 배열로 변환
print("new_data : ",new_data)
new_data_poly = poly.transform(new_data)
print("new_data_poly : ",new_data_poly)
prediction = model.predict(new_data_poly)
print(prediction)

# 잔차 구하기 
y_mean = np.mean(y_test) 
# # y 평균값 # $\sum(y 예측값 - y 평균값)^2$ = 예측값에 대한 편차 
nomerator = np.sum(np.square(y_test - y_pred)) # $sum(y 관측값 - y 평균값)^2$ 
denominator = np.sum(np.square(y_test - y_mean)) 
accuracy = 1 - nomerator / denominator 
print(accuracy)


# # 그래프 그리기
# plt.figure(figsize=(8, 6))

# # 실제값과 예측값의 산점도 그리기
# plt.scatter(y_test, y_pred, color='blue', alpha=0.7)
# plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linewidth=2)  # 대각선 기준선

# plt.title("실제값 대 예측값")
# plt.xlabel("실제값")
# plt.ylabel("예측값")
# plt.show()