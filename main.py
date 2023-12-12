from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

import numpy as np
import joblib

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def hello():
    return "hello"

class bald_persent_info(BaseModel):
	age: float 
	gender: int 
	is_married: int 
	is_hereditary: int 
	weight: float 
	height: float 
	is_smoker: int 
	stress: int 
    

from bald_persent_score import complete_model
from sklearn.preprocessing import PolynomialFeatures

@app.post("/bald_persent_predict")
async def bald_persent_predict(data : bald_persent_info):
	data_dict = {				
				"age":data.age, 
				"gender":data.gender, 
				"is_married":data.is_married,                                                    
				"is_hereditary":data.is_hereditary, 
				"weight":data.weight, 
				"height":data.height, 
				"is_smoker":data.is_smoker,
				"stress":data.stress
			}
	
	data = np.array([
            		data_dict["age"], 
                  	data_dict["gender"], 
                    data_dict["is_married"], 
                    data_dict["is_hereditary"], 
                    data_dict["weight"], 
                    data_dict["height"], 
                    data_dict["is_smoker"], 
                    data_dict["stress"]]).reshape(1, -1)
    
	poly = PolynomialFeatures(degree=2)
	data = poly.fit_transform(data)
	predict = complete_model.predict(data)

	result = {"predict":predict.tolist()[0]}
	return result

if __name__=='__main__': 
    uvicorn.run(app, host='0.0.0.0', port = 8000)


#uvicorn main:app --reload

