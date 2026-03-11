# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 12:01:20 2024

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

start = time.perf_counter()

with open(".\\SETTINGS.json", "r") as file:
    SETTINGS = json.load(file)

if SETTINGS["CLEAN_DATA_AVAILABLE"]:
    Feats = pd.read_csv(SETTINGS["CLEAN_DATA_PATH"])
else:
    GET_ALL_FEATS(SETTINGS["RAW_DATA_PATH"])
    Feats = pd.read_csv(SETTINGS["CLEAN_DATA_PATH"])


train = pl.read_csv(SETTINGS["RAW_DATA_PATH"])
tr = pd.read_csv(SETTINGS["RAW_DATA_PATH"])


def quadratic_weighted_kappa(y_true, y_pred):

        # For lgb
        y_true = y_true + a
        y_true = y_true.round().clip(1,6)
        y_pred = (y_pred + a).clip(1,6).round()


        y_true = y_true.round()
        y_pred = y_pred.round()
        qwk = cohen_kappa_score(y_true, y_pred, weights="quadratic")
        return 'QWK', qwk, True


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

def quadratic_weighted_kappa_cls(y_true, y_pred):
        y_pred = y_pred.argmax(axis = -1)
    
        qwk = cohen_kappa_score(y_true, y_pred, weights="quadratic")
        return 'QWK', qwk, True


class params:
    reg_param = {
             "objective": qwk_obj,
             "metrics": "None",
             'n_estimators': 1400,
             'num_leaves': 10,
             'learning_rate': 0.05,
             'colsample_bytree': 0.3,
             'reg_alpha': 10,
             'reg_lambda': 2,
             'max_depth': 5,
             "n_jobs": -1,
             'force_col_wise':True,
             'verbosity': 1,
             "class_weight":"balanced",
             "extra_trees":True,
             "random_state":66
     }
    
    cls_param = {
             "metrics": "None",
             'n_estimators': 1200,
             'num_leaves': 11,
             'learning_rate': 0.04,
             'colsample_bytree': .4,
             'reg_alpha': 2,
             'reg_lambda': .7,
             'max_depth': 6,
             "n_jobs": -1,
             'force_col_wise':True,
             'verbosity': 1,
             "class_weight":"balanced",
             "extra_trees":True,
             "random_state":66
     }
    reg_cb = [log_evaluation(period=50), early_stopping(stopping_rounds=100,first_metric_only=True)] 
    cls_cb = [log_evaluation(period=50), early_stopping(stopping_rounds=100,first_metric_only=True)]
    cls_cb2 = [log_evaluation(period=50), early_stopping(stopping_rounds=75,first_metric_only=True)]
    path = SETTINGS["SAVE_MODEL_DIR"]


def TRAINING(Type,params,callbacks,metric_fxn,path,Feats,train=train,split=5,state=66):
    imps = {}
    skf = StratifiedKFold(split, shuffle = True, random_state = state)
    if Type == "regression":
        p = np.zeros(len(train))
        name = "reg"
    else:
        p = np.zeros(len(train))
        prob = np.zeros((len(train), 6))
        name = "cls"
    
    for idx, (tri, tsi) in enumerate(skf.split(train["full_text"],train[:,"score"])):
        
        if Type == "regression":
            mod = lgbm.LGBMRegressor(**params)
            mod.fit(Feats.iloc[tri], tr.score.iloc[tri]-a,
                          eval_set = [(Feats.iloc[tri], tr.score.iloc[tri]-a),
                                      (Feats.iloc[tsi], tr.score.iloc[tsi]-a)],
                          eval_names = ["train", "test"], callbacks = callbacks,
                          eval_metric = metric_fxn)
            preds = mod.predict(Feats.iloc[tsi])+a
            p[tsi] = preds
            preds = preds.clip(1,6).round()
            
        else:
            mod = lgbm.LGBMClassifier(**params)
            
            mod.fit(Feats.iloc[tri], tr.score.iloc[tri],
                          eval_set = [(Feats.iloc[tri], tr.score.iloc[tri]),
                                      (Feats.iloc[tsi], tr.score.iloc[tsi])],
                          eval_names = ["train", "test"], callbacks = callbacks,
                          eval_metric = metric_fxn)
            preds = mod.predict(Feats.iloc[tsi])
            p[tsi] = preds
            prob[tsi] = mod.predict_proba(Feats.iloc[tsi])
        
        imps[idx] = pd.DataFrame({"imps":mod.feature_importances_, "cols":Feats.columns})
        #score = cohen_kappa_score(preds, tr.score.iloc[tsi], weights = "quadratic")
        pickle.dump(mod, open(path + f"{name}_{idx}.pkl", "wb"))
        #cm = confusion_matrix(tr.score.iloc[tsi], preds)
        #ConfusionMatrixDisplay(cm, display_labels = [i for i in range(1,7)]).plot()
        #plt.title(f"{name} {idx} {score:.5f}")
        #plt.show()
    
    if Type == "regression":
        return imps,p
    else:
        return imps,p,prob
    
## Training Classifier
cls_imps, pcls,prob = TRAINING(
    "classification",
    params.cls_param,
    params.cls_cb,
    quadratic_weighted_kappa_cls,
    params.path,
    Feats=Feats)

print(cohen_kappa_score(tr["score"], pcls, weights = "quadratic")) # .787734756352525

## Adding Probabilities of Classifier for Regressor
Feats = Feats.join(pd.DataFrame(prob, columns = [f"{i}_" for i in range(1,7)]))

## Training Regressor
reg_imps, p = TRAINING(
    "regression",
    params.reg_param,
    params.reg_cb,
    quadratic_weighted_kappa,
    params.path,
    Feats=Feats)

print(cohen_kappa_score(tr["score"], p.clip(1,6).round(), weights = "quadratic")) # .8142769299512969


## Feature selection based upon Importance
def Feature_Selection(imps, n, n_models):
    ex = imps[0]
    ex = ex[ex["imps"]>n].sort_values(by = "imps", ascending = False)
    
    for i in range(1,n_models):
        ex1 = imps[i]
        ex1 = ex1[ex1["imps"]>n].sort_values(by = "imps", ascending = False)
        ex = pd.concat([ex,ex1])
        
    ex = ex.sort_values(by = "imps", ascending = False)
    imps_ = ex.cols.unique()
    return imps_

# Regressor Feature Selection
all_reg_imps = Feature_Selection(reg_imps, 0, 5)

# Classifier Feature Selection
all_cls_imps = Feature_Selection(cls_imps, 5, 5)

# SAVING FEATURES

pickle.dump(all_reg_imps, open(SETTINGS["FEATURE_SELECTION_DIR"]+"reg_imps.pkl", "wb"))
pickle.dump(all_cls_imps, open(SETTINGS["FEATURE_SELECTION_DIR"]+"cls_imps.pkl", "wb"))

#Removing Probabilities of previous Classifier
Feats = Feats.iloc[:, :-6]

# Selecting only Important classifier features
FeatsC = Feats.loc[:, all_cls_imps].copy()

# Training Model again, NOTE: New Callback with EarlyStopping=75
cls_imps, pcls,prob = TRAINING(
    "classification",
    params.cls_param,
    params.cls_cb2,
    quadratic_weighted_kappa_cls,
    params.path,
    Feats=FeatsC)

print(cohen_kappa_score(tr["score"], pcls, weights = "quadratic")) # 0.7874222591863567

# Adding Probabilities of Classifier 
Feats = Feats.join(pd.DataFrame(prob, columns = [f"{i}_" for i in range(1,7)]))

# Selecting only important features for Regressor
Feats = Feats.loc[:, all_reg_imps]

reg_imps, p = TRAINING(
    "regression",
    params.reg_param,
    params.reg_cb,
    quadratic_weighted_kappa,
    params.path,
    Feats=Feats)

print(cohen_kappa_score(tr["score"], p.clip(1,6).round(), weights = "quadratic")) # 0.8158797934798527
#cm = confusion_matrix(tr["score"], p.clip(1,6).round())
#ConfusionMatrixDisplay(cm, display_labels = [i for i in range(1,7)]).plot()

end = time.perf_counter()
print("*"*45)
print(f"Took {(end-start)/60:.2f} minutes to complete the Training")
print("*"*45)