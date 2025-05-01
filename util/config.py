import os, sys

now_dir = os.getcwd()
sys.path.append(now_dir)

datasetPath = os.path.join(now_dir,'dataset.csv')
csvPath = os.path.join(now_dir,'test.csv')

api_port = 6666
modelPath = os.path.join(now_dir,'talmo.pkl')

from pydantic import BaseModel, Field
from typing import Literal

class UserInput(BaseModel):
    age: str
    gender: Literal["male", "female"]
    is_hereditary: Literal["Yes", "No"]
    stress: Literal["Level 1", "Level 2", "Level 3", "Level 4"]
    is_married: Literal["Yes", "No"]
    weight: float
    height: float
    is_smoker: Literal["Yes", "No"]

class Config:
    def __init__(self):
        self.datasetPath = datasetPath
        self.csvPath = csvPath

        self.api_port = api_port
        self.modelPath = modelPath