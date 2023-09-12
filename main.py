from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

import numpy as np

app = FastAPI()

@app.get("/")
def hello():
    return "hello"

@app.get("/test")
def test():
	x = 1
	return x

class bald_persent_info(BaseModel):
	age: float 
	gender: int 
	is_married: int 
	is_hereditary: int 
	weight: float 
	height: float 
	is_smoker: int 
	stress: int 
    

from bald_persent_score.bald_score import accuracy_result,predict_result

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
	
	data = np.array([data_dict["age"], data_dict["gender"], data_dict["is_married"], data_dict["is_hereditary"], data_dict["weight"], data_dict["height"], data_dict["is_smoker"], data_dict["stress"]]).reshape(1, -1)
	predict = predict_result(data)
	
	now_acc = accuracy_result()
	#now_accuracy = bald_score.accuracy

	result = {"now_acc":now_acc, "predict":predict.tolist()[0]}
	# result = {"predict_result":bald_persent_result, "now_accuracy":now_accuracy}
	# return result
	return result

if __name__=='__main__': 
    uvicorn.run(app, host='0.0.0.0', port = 8000)


#uvicorn main:app --reload

