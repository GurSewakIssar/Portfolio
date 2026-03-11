# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 12:24:40 2024

@author: gurse
"""

import pandas as pd # '2.2.1'
import polars as pl # '0.20.31'
import regex as re
import pickle       # '4.0'
import time
import numpy as np #'1.26.4'
import matplotlib.pyplot as plt
import string
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer # '1.4.2'
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import cohen_kappa_score,confusion_matrix, ConfusionMatrixDisplay
from scipy.sparse import coo_matrix, hstack #'1.13.0'
import warnings
from lightgbm import log_evaluation, early_stopping
import lightgbm as lgbm # '4.3.0' 
from prepare_data import GET_ALL_FEATS
import json

# with open(".\\Submission_Model\\SETTINGS.json", "r") as file:
with open(".\\SETTINGS.json", "r") as file:
    SETTINGS = json.load(file)


GET_ALL_FEATS(SETTINGS["TEST_DATA_PATH"], mode = "predict")
Feats = pd.read_csv(SETTINGS["CLEAN_DATA_PATH"])

all_reg_imps = pickle.load(open(SETTINGS["FEATURE_SELECTION_DIR"]+"reg_imps.pkl", "rb"))
all_cls_imps = pickle.load(open(SETTINGS["FEATURE_SELECTION_DIR"]+"cls_imps.pkl", "rb"))

test = pd.read_csv(SETTINGS["TEST_DATA_PATH"])

def qwk_obj(y_true, y_pred):
    labels = y_true + a
    preds = y_pred + a
    preds= preds.clip(1,6)
    f = 1/2*np.sum((preds-labels)**2)
    g = 1/2*np.sum((preds-a)**2+b)
    df = preds - labels 
    dg = preds - a
    grad = (df/g - f*dg/g**2)*len(labels)
    hess = np.ones(len(labels))
    return grad, hess
a = 2.998 
b = 1.092 

FeatsC = Feats.loc[:, all_cls_imps].copy()
probabilities = np.zeros((5,len(test), 6))

for idx in range(5):
    mod = pickle.load(open(SETTINGS["LOAD_MODEL_DIR"]+f"cls_{idx}.pkl", "rb"))
    probabilities[idx] = mod.predict_proba(FeatsC)

probabilities = np.mean(probabilities, axis = 0)

Feats = Feats.join(pd.DataFrame(probabilities, columns = [f"{i}_" for i in range(1,7)]))
Feats = Feats.loc[:, [str(i) for i in all_reg_imps]]

predictions = np.zeros((5,len(test)))

for idx in range(5):
    mod = pickle.load(open(SETTINGS["LOAD_MODEL_DIR"]+f"reg_{idx}.pkl", "rb"))
    predictions[idx] = mod.predict(Feats)+a

predictions = np.mean(predictions, axis = 0)

sub = pd.DataFrame()
sub["essay_id"] = test["essay_id"]
sub["score"] = predictions.clip(1,6).round().astype(int)

sub.to_csv(SETTINGS["PREDICTION_SAVE_PATH"], index = False)

