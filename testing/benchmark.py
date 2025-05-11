from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
# from xgboost import XGBClassifier
import pandas as pd

# import config as gConfig
# config = gConfig.Config()
# path = config.csvPath
# df = pd.read_csv(path)

# models = {
#     # "Random Forest": RandomForestClassifier(random_state=42),
#     # "Logistic Regression": LogisticRegression(random_state=42),
#     # "Support Vector Machine": SVC(random_state=42),
#     # "Gradient Boosting": GradientBoostingClassifier(random_state=42),

#     "Random Forest": RandomForestClassifier(random_state=42, n_estimators=100, class_weight='balanced'),
#     "Logistic Regression": LogisticRegression(random_state=42, max_iter=1000, class_weight='balanced', C=1.0),
#     "Support Vector Machine": SVC(random_state=42, class_weight='balanced', probability=True),
#     "Gradient Boosting": GradientBoostingClassifier(random_state=42, n_estimators=100),
#     # Add more models here as needed
# }

# columns = [
#             'age',
#             'gender',
#             'is_hereditary',
#             'stress', 
#             'is_married', 
#             'weight',
#             'height',
#             'is_smoker'
#             ]
# df_dummies = pd.get_dummies(df[columns])

# from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
# m_lda = LinearDiscriminantAnalysis()

# y = df['bald_prob']
# X = df

# y = y.T.drop_duplicates().T 

# print(X)
# print(y)

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# results = {
#     "Model": [],
#     "Accuracy": []
# }

# for name, model in models.items():
#     model.fit(X_train, y_train)
#     y_pred = model.predict(X_test)
#     accuracy = accuracy_score(y_test, y_pred)
    
#     # Store results
#     results["Model"].append(name)
#     results["Accuracy"].append(accuracy)

# # Create a DataFrame from results
# results_df = pd.DataFrame(results)

# print(results_df)