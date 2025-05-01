from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

import pandas as pd
import config as gConfig
config = gConfig.Config()
path = config.csvPath
df = pd.read_csv(path)

columns = [
            'age',
            'gender',
            'is_hereditary',
            'stress', 
            'is_married', 
            'weight',
            'height',
            'is_smoker'
            ]

df_dummies = pd.get_dummies(df[columns])

X = df_dummies
y = df['bald_prob']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

report = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy}')
print(f'Report:\n{report}')

import pickle
with open('talmo.pkl', 'wb') as f:
    pickle.dump(model, f)
