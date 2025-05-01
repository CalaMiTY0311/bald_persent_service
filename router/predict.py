import os, sys

now_dir = os.getcwd()
sys.path.append(now_dir)
print(now_dir)

from fastapi import APIRouter, HTTPException
import pandas as pd
import pickle

import util.config as gConfig

config = gConfig.Config()
inputModel = gConfig.UserInput

router = APIRouter(
    prefix="/predict"
)

with open('talmo.pkl', 'rb') as f:
    model = pickle.load(f)

@router.post("")
async def predict_baldness(input: inputModel):
    try:
        user_df = pd.DataFrame([{
            "age": input.age, 
            "gender": input.gender, 
            "is_married": input.is_married,
            "is_hereditary": input.is_hereditary, 
            "weight": input.weight, 
            "height": input.height, 
            "is_smoker": input.is_smoker,
            "stress": input.stress
        }])
        user_dummies = pd.get_dummies(user_df)
        
        columns = [
            'age', 'gender', 'is_hereditary', 'stress', 
            'is_married', 'weight', 'height', 'is_smoker'
        ]
        df_sample = pd.read_csv(config.csvPath)
        df_dummies_sample = pd.get_dummies(df_sample[columns])
        feature_names = df_dummies_sample.columns.tolist()
        
        for col in feature_names:
            if col not in user_dummies.columns:
                user_dummies[col] = 0
        
        user_dummies = user_dummies[feature_names]
        
        # 예측 수행
        prediction = model.predict(user_dummies)[0]
        prediction_proba = model.predict_proba(user_dummies)[0]
        
        # 결과 반환
        result = {"prediction": prediction}
        
        # 확률 추가
        if 'High' in model.classes_ and 'Low' in model.classes_:
            high_index = list(model.classes_).index('High')
            low_index = list(model.classes_).index('Low')
            result["high_probability"] = round(prediction_proba[high_index] * 100, 2)
            result["low_probability"] = round(prediction_proba[low_index] * 100, 2)
        
        return result
    
    except Exception as e:
        print("e : ", e)
        raise HTTPException(status_code=500, detail=f"예측 중 오류가 발생했습니다")
