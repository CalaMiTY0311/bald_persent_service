import os, sys

now_dir = os.getcwd()
sys.path.append(now_dir)
print(now_dir)

import pandas as pd
import numpy as np
from scipy import stats

import util.config as gConfig

config = gConfig.Config()
path = gConfig.csvPath

df = pd.read_csv(path)

df['bald_prob'] = df['bald_prob'].map({'High': 1, 'Low': 0})

corr_age = df['bald_prob'].corr(df['age'].str.replace('+', '').astype(int), method="spearman")
corr_stress = df['bald_prob'].corr(df['stress'].str.replace('Level ', '').astype(int), method="spearman")

corr_married, p_married = stats.pointbiserialr(df['is_married'].map({'Yes': 1, 'No': 0}), df['bald_prob'])
corr_hereditary, p_hereditary = stats.pointbiserialr(df['is_hereditary'].map({'Yes': 1, 'No': 0}), df['bald_prob'])
corr_smoking, p_smoking = stats.pointbiserialr(df['is_smoker'].map({'Yes': 1, 'No': 0}), df['bald_prob'])

corr_weight = df['bald_prob'].corr(df['weight'], method='pearson')
corr_height = df['bald_prob'].corr(df['height'], method='pearson')

print(f"연령과 탈모 확률의 상관관계: {corr_age}")
print(f"스트레스와 탈모 확률의 상관관계: {corr_stress}")
print('\n')
print(f"결혼 여부와 탈모 확률의 상관관계: {corr_married}, {p_married}")
print(f"유전적 요인과 탈모 확률의 상관관계: {corr_hereditary}, {p_hereditary}")
print(f"흡연 여부와 탈모 확률의 상관관계: {corr_smoking}, {p_smoking}")
print('\n')
print(f"체중과 탈모 확률의 상관관계: {corr_weight}")
print(f"키와 탈모 확률의 상관관계: {corr_height}")

# 상관계수 값의 의미:

# 1에 가까울수록: 강한 양의 상관관계 (한 변수가 증가하면 다른 변수도 함께 증가)
# 0에 가까울수록: 상관관계가 약하거나 없음 (두 변수 간에 선형적 관계가 없음)
# -1에 가까울수록: 강한 음의 상관관계 (한 변수가 증가하면 다른 변수는 감소)


# 상관계수 범위별 해석:

# 0.7 ~ 1.0: 매우 강한 양의 상관관계
# 0.5 ~ 0.7: 중간 정도의 양의 상관관계
# 0.3 ~ 0.5: 약한 양의 상관관계
# -0.3 ~ 0.3: 상관관계가 매우 약하거나 없음
# -0.5 ~ -0.3: 약한 음의 상관관계
# -0.7 ~ -0.5: 중간 정도의 음의 상관관계
# -1.0 ~ -0.7: 매우 강한 음의 상관관계
