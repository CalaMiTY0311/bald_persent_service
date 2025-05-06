import pandas as pd
import config as gConfig
config = gConfig.Config()

path = config.datasetPath

df = pd.read_csv(path)

########################################결측 치 제거################################################
df.drop([
    'job_role',
    'province',
    'salary',
    'shampoo',
    'education'
    ],axis = 1,inplace =True)   # 행 제거

df_na = df.isnull().sum()
print("결측치 인덱스 수 : ", df_na)

mean_age = df["age"].mean()
df['age'].fillna(round(mean_age), inplace=True)

mean_weight = df['weight'].mean()
df['weight'].fillna(mean_weight, inplace=True)
df['weight'] = df['weight'].round(2)

mean_height = df['height'].mean()
df['height'].fillna(mean_height, inplace=True)
df['height'] = df['height'].round(2)

mean_stress = df['stress'].mean()
df['stress'].fillna(round(mean_stress), inplace=True)

df_null = df[df['bald_prob'].isnull()]
df = df.drop(df_null.index)

df_na = df.isnull().sum()
print("정제 후 결측치 인덱스 수 : ", df_na)

df = df.dropna()  #NAN/빈값있는 행 제거

########################################데이터 전처리################################################
df_err = df[df['age'] < 10]
df = df[~df['age'].isin(df_err['age'])]

df['age'] = df['age'].apply(lambda x: '0+' if x < 10
                                  else '10+' if 10 <= x < 20
                                  else '20+' if 20 <= x < 30
                                  else '30+' if 30 <= x < 40
                                  else '40+' if 40 <= x < 50
                                  else '50+' if 50 <= x < 60
                                  else '60+' if 60 <= x < 70
                                  else '70+' if 70 <= x < 80
                                  else '80+')

df['stress'] = df['stress'].apply(lambda x: "Level 1" if x <= 3
                                                     else "Level 2" if 4 <= x <= 6
                                                     else "Level 3" if 7 <= x <= 9
                                                     else "Level 4")

df['is_married'] = df['is_married'].apply(lambda x: 'Yes' if x == 1 else 'No')
df['is_smoker'] = df['is_smoker'].apply(lambda x: 'Yes' if x == 1 else 'No')
df['is_hereditary'] = df['is_hereditary'].apply(lambda x: 'Yes' if x == 1 else 'No')

df['bald_prob'] = df['bald_prob'].apply(lambda x: 'Low' if x <= 0.5
                                        else 'High')

df.to_csv('test.csv')


