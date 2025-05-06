import os, sys

now_dir = os.getcwd()
sys.path.append(now_dir)

datasetPath = os.path.join(now_dir,'dataset.csv')
csvPath = os.path.join(now_dir,'test.csv')

api_port = 1542
modelPath = os.path.join(now_dir,'talmo.pkl')

from pydantic import BaseModel
from typing import Literal, Optional

class UserInput(BaseModel):
    age: Optional[str] = None
    gender: Optional[Literal["male", "female"]] = None
    is_hereditary: Optional[Literal["Yes", "No"]] = None
    stress: Optional[Literal["Level 1", "Level 2", "Level 3", "Level 4"]] = None
    is_married: Optional[Literal["Yes", "No"]] = None
    weight: Optional[float] = None
    height: Optional[float] = None
    is_smoker: Optional[Literal["Yes", "No"]] = None

class Config:
    def __init__(self):
        self.datasetPath = datasetPath
        self.csvPath = csvPath

        self.api_port = api_port
        self.modelPath = modelPath