import traceback
import os, sys

now_dir = os.getcwd()
sys.path.append(now_dir)
print(now_dir)

from fastapi import APIRouter, HTTPException
import pandas as pd
import pickle

from util.generator import getPersent

import util.config as gConfig
config = gConfig.Config()
inputModel = gConfig.UserInput

predict = APIRouter(
    prefix="/predict"
)

with open('talmo.pkl', 'rb') as f:
    model = pickle.load(f)

@predict.post("")
async def default(input: inputModel):
    print(input)
    try:
        missing_fields = []
        
        if not input.age:
            missing_fields.append("age")
        if not input.gender:
            missing_fields.append("gender")
        if not input.is_married:
            missing_fields.append("is_married")
        if not input.is_hereditary:
            missing_fields.append("is_hereditary")
        if not input.weight or input.weight <= 0:
            missing_fields.append("weight")
        if not input.height or input.height <= 0:
            missing_fields.append("height")
        if not input.is_smoker:
            missing_fields.append("is_smoker")
        if not input.stress:
            missing_fields.append("stress")
        
        if missing_fields:
            return {
                "success": False,
                "data": f"필드가 누락되었습니다: {', '.join(missing_fields)}"
            }
        
        input_dict = {
            "age": input.age,
            "gender": input.gender,
            "is_married": input.is_married,
            "is_hereditary": input.is_hereditary,
            "weight": float(input.weight),
            "height": float(input.height),
            "is_smoker": input.is_smoker,
            "stress": input.stress
        }
        prediction_result = getPersent(input_dict)
        
        return { 
            "success": True, 
            "data": prediction_result
        }
    
    except Exception as e:
        traceback.print_exc()
        return {
            "success": False,
            "data": f"서버 오류가 발생했습니다: {str(e)}"
        }
