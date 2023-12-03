import os
import joblib

dir = os.path.dirname(__file__)

path = os.path.join(dir, 'complete_model.pkl')

complete_model = joblib.load(path)
