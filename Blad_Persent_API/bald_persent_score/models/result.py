import numpy as np
import pandas as pd
from sklearn import datasets
#
from sklearn import model_selection
from sklearn.linear_model import Ridge
from sklearn import metrics

from lr_score import lr_score
from rf_score import rf_score
from lasso_score import lasso_score
from ridge_score import ridge_score
from svm_score import svm_score

lr_score()
#rf_score()
lasso_score()
ridge_score()
svm_score()