from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

import numpy as np

app = FastAPI()

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

from bald_persent_score import bald_score
@app.get("/bald_persent_predict")
async def bald_persent_predict(data : bald_persent_info):
	bald_data = np.array([	data.age, 
                        	data.gender, 
                        	data.is_married,                                                    
                            data.is_hereditary, 
                        	data.weight, 
                            data.height, 
                            data.is_smoker,
                            data.stress
                        	]).reshape(1, -1)
	bald_poly = bald_score.poly
	bald_model = bald_score.complete_model
	bald_data_poly = bald_poly.transform(bald_data)
	bald_predict = bald_model.predict(bald_data_poly)
	
if __name__=='__main__': 
    uvicorn.run(app, host='0.0.0.0', port = 8000)


#uvicorn main:app --reload

