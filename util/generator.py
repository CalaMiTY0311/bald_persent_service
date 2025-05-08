import pickle
import pandas as pd
import numpy as np

def getPersent(data):
    with open('talmo.pkl', 'rb') as f:
        model = pickle.load(f)
    
    df = pd.DataFrame([data])
    df = pd.get_dummies(df)

    missing_features = set(model.feature_names_in_) - set(df.columns)
    extra_features = set(df.columns) - set(model.feature_names_in_)
    
    for feature in missing_features:
        df[feature] = 0
    
    X_predict = df[model.feature_names_in_]
    
    prediction = model.predict(X_predict)[0]
    probabilities = model.predict_proba(X_predict)[0]
    
    result = {
        "prediction": prediction
    }
    
    for i, class_label in enumerate(model.classes_):
        result[f"{class_label}_probability"] = round(probabilities[i] * 100, 2)
    
    return result

if __name__ == "__main__":
    data = {
        "age": "30+",
        "gender": "female", 
        "is_married": "No",
        "is_hereditary": "Yes", 
        "weight": 75.5, 
        "height": 175.0, 
        "is_smoker": "No",
        "stress": "Level 3"
    }
    
    result = getPersent(data)
    
    print(f"결과: {result['prediction']}")
    
    for key, value in result.items():
        if key.endswith('_probability'):
            print(f"{key}: {value}%")