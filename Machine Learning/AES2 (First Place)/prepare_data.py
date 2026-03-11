# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 11:32:16 2024

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
import json


with open(".\\SETTINGS.json", "r") as file:
    SETTINGS = json.load(file)


def remove__(x):
    """Removes multiple spaces"""
    return re.sub("\s{2,100000}", "", x)


def clean_row_for_split(row):
    """Preprocessing required to split the words"""
    row = row.lower()
    row = re.sub("[<>\|\^\@\*²¹©\$\d\&,\/\.\(\)\[\]\s\&\%\#\!\-\_\=\+\:\?\"';]"," ", row)
    row = re.sub("\s{2,10000}", " ", row)
    row = row.split(" ")
    return row

al = pickle.load(open(SETTINGS["CORRECT_WORDS_PATH"], "rb"))
def Spelling_Errors(row):
    """Returns spelling errors as percentage of total words"""
    num = 0 
    for tok in row:
        if tok not in al:
            num+=1

    return num/len(row)


def Unique_words_prcnt(row):
    """Returns Percentage of unique words"""
    return len(set(row))/len(row)


def span_length(x, gap_width = 10): 
    """
    Returns Sum  and Count of all the Source/Quoted text with length > gap width.
    NOTE, quoted text also contains quotes so their length always contains 2 more characters.
    Thats why, while returning I subtracted 2 from length. It is just to make more accurate 
    measurements.
    """
    num = 0
    cnt = 0
    for sp in x:
        gap = sp.span()[1] - sp.span()[0] 
        if gap > gap_width:
            num+= gap
            cnt+=1
        
    return num-(cnt*2), cnt


def find_span_length(x):
    """
    Find all the spans of double quoted text and pass it to `span_length` function
    to get total span length and number of spans.
    """
    spans = list(re.finditer("\"[\w\s\?\[\]\(\)\-\!\:\;\']+\"", x))
    return (span_length(spans))


def PreprocessText(x):
    x = x.lower()
    x = re.sub("[0-9\&\,\.\_\~\+\-\(\)\*#\$\%@!\?:;`\|\"'\[\]\/\\\]", " ", x)
    x = re.sub("[\s\.]{2,100000}", " ", x)
    return x


def ParaPreprocessing(train):
    
    train = train.explode("paragraph")
    train = train.with_columns(pl.col("paragraph").map_elements(clean_row_for_split).alias("p_cln"))
    

    train = train.with_columns(pl.col("paragraph").map_elements(
        lambda x: len(x), return_dtype=int).alias("paragraph_len"))
    
    train = train.with_columns(pl.col("paragraph").map_elements(
        lambda x: len(x.split(".")), return_dtype=int).alias("paragraph_sent_cnt"))
    
    train = train.with_columns(pl.col("paragraph").map_elements(
        lambda x: len(x.split(" ")), return_dtype=int).alias("paragraph_word_cnt"))
    
    train = train.with_columns(pl.col("p_cln").map_elements(
        Spelling_Errors, return_dtype=float).alias("paragraph_errors"))
    
    
    li = []
    lii = []
    for row in train[:,"full_text"]:
        j,jj = find_span_length(row)
        li.append(j)
        lii.append(jj)
    
    train = train.with_columns(pl.col("paragraph").map_elements(lambda x: len(x), return_dtype = int).alias("plen"))
    
    ## SPAN FEATURES FOR PARAGRAPH
    ## span length
    train = train.with_columns(pl.Series("spans", li).alias("spans"))
    
    # spans count
    train = train.with_columns(pl.Series("spansN", lii).alias("spansN"))
    
    # percentage of spans in a paragraph
    train = train.with_columns((pl.col("spans")/pl.col("plen")).alias("spans%"))
    
    # Average span length
    train = train.with_columns((pl.col("spans")/pl.col("spansN")).alias("spansAvg"))
    
    return train


# feature_eng
paragraph_fea = ['paragraph_len','paragraph_sent_cnt','paragraph_word_cnt',
                 "paragraph_errors",]# "unique_words_prcnt"]


def ParaFeatures(train_tmp):
    aggs = [
        *[pl.col("spans").max().alias("SP_Max")],
        *[pl.col("spans").mean().alias("SP_Mean")],
        *[pl.col("spans").sum().alias("SP_Sum")],
        
        *[pl.col("spansN").max().alias("SPN_Max")],
        *[pl.col("spansN").mean().alias("SPN_Mean")],
       #*[pl.col("spansN").sum().alias("SPN_Sum")],
        
        *[pl.col("spans%").max().alias("SP%_Max")],
        *[pl.col("spans%").mean().alias("SP%_Mean")],
        *[pl.col("spans%").sum().alias("SP%_Sum")],
        
        *[pl.col("spansAvg").max().alias("SPAvg_Max")],
        *[pl.col("spansAvg").mean().alias("SPAvg_Mean")],
        *[pl.col("spansAvg").sum().alias("SPAvg_Sum")],
        
        *[pl.col('paragraph').filter(pl.col('paragraph_len') >= i).count().alias(f"paragraph_>{i}_cnt")
          for i in [i for i in range(0, 650, 50)]],#
        *[pl.col('paragraph').filter(pl.col('paragraph_len') <= i).count().alias(f"paragraph_<{i}_cnt")
          for i in [25,49]], #range(25, 650, 50)],#[.01,.02,.03,.05,.1,.2,.4,.6]
        
        *[pl.col('paragraph').filter(pl.col('paragraph_errors') > i).count().alias(f"paragraph_er_>{i}_cnt")
          for i in [i for i in [0,.005,.01,.02,.03,.05,]]],
        
        
        *[pl.col(fea).max().alias(f"{fea}_max") for fea in paragraph_fea],
        *[pl.col(fea).mean().alias(f"{fea}_mean") for fea in paragraph_fea],
        *[pl.col(fea).min().alias(f"{fea}_min") for fea in paragraph_fea],
        *[pl.col(fea).sum().alias(f"{fea}_sum") for fea in paragraph_fea if fea != "unique_words_prcnt"],
        *[pl.col(fea).first().alias(f"{fea}_first") for fea in paragraph_fea],
        *[pl.col(fea).last().alias(f"{fea}_last") for fea in paragraph_fea],
        #*[pl.col(fea).kurtosis().alias(f"{fea}_kurtosis") for fea in paragraph_fea],
        *[pl.col(fea).quantile(0.25).alias(f"{fea}_q1") for fea in paragraph_fea],
        *[pl.col(fea).quantile(0.5).alias(f"{fea}_q2") for fea in paragraph_fea],
        *[pl.col(fea).quantile(0.75).alias(f"{fea}_q3") for fea in paragraph_fea],
        ]
    df = train_tmp.group_by(['essay_id'], maintain_order=True).agg(aggs)

    df = df.to_pandas()

    return df, train_tmp


def SentPreprocessing(train):
    train = train.with_columns(pl.col("full_text").str.split(".").alias("sentence"))
    train = train.explode("sentence")
    
    train = train.with_columns(pl.col("sentence").map_elements(clean_row_for_split).alias("s_cln"))
    
    train = train.with_columns(pl.col("sentence").map_elements(
        lambda x: len(x), return_dtype=int).alias("sentence_len"))
    
    train = train.with_columns(pl.col("sentence").map_elements(
        lambda x: len(x.split(" ")), return_dtype=int).alias("sentence_word_cnt"))
    

    train = train.with_columns(pl.col("s_cln").map_elements(
        Spelling_Errors, return_dtype=float).alias("sentence_errors"))


    train = train.with_columns(pl.col("s_cln").map_elements(
        Unique_words_prcnt, return_dtype=float).alias("s_unique_words_prcnt"))

    return train


sent_feats = ["sentence_len", "sentence_word_cnt", "sentence_errors", "s_unique_words_prcnt"]
def SentFeatures(train):
    
    aggs = [
        *[pl.col(["sentence"]).filter(pl.col("sentence_len")>=i).count().alias(f"sent_len>{i}") 
                                    for i in range(0, 160, 10)],
        *[pl.col(["sentence"]).filter(pl.col("sentence_len")<=i).count().alias(f"sent_len<{i}") 
                                    for i in [15,50]], #range(15, 160, 30)],#
        
        *[pl.col('sentence').filter(pl.col('sentence_errors') > i).count().alias(f"sentence_er_>{i}_cnt")
          for i in [i for i in [.01,.02,.03,.05,]]],
        

        *[pl.col(fea).max().alias(f"{fea}_max") for fea in sent_feats],
        *[pl.col(fea).mean().alias(f"{fea}_mean") for fea in sent_feats],
        *[pl.col(fea).min().alias(f"{fea}_min") for fea in sent_feats],
        *[pl.col(fea).sum().alias(f"{fea}_sum") for fea in sent_feats if fea != "s_unique_words_prcnt"],
        *[pl.col(fea).first().alias(f"{fea}_first") for fea in sent_feats],
        *[pl.col(fea).last().alias(f"{fea}_last") for fea in sent_feats],
        #*[pl.col(fea).kurtosis().alias(f"{fea}_kurtosis") for fea in sent_feats],
        *[pl.col(fea).quantile(0.25).alias(f"{fea}_q1") for fea in sent_feats],
        *[pl.col(fea).quantile(0.5).alias(f"{fea}_q2") for fea in sent_feats],
        *[pl.col(fea).quantile(0.75).alias(f"{fea}_q3") for fea in sent_feats],
        ]
    
    train = train.group_by(["essay_id"], maintain_order = True).agg(aggs)
    df = train.to_pandas()
    return df


def WordPreprocessing(train):
    train = train.with_columns(pl.col("full_text").str.split(" ").alias("word"))
    train = train.explode("word")
    train = train.with_columns(pl.col("word").map_elements(
        lambda x: len(x), return_dtype=int).alias("word_len"))
    train = train.filter(pl.col("word_len")>0)
    return train


def WordFeatures(train):
    aggs = [
        *[pl.col(["word"]).filter(pl.col("word_len")>=i).count().alias(f"word_len>{i}") 
                                    for i in range(1, 16)],
        *[pl.col("word_len").max().alias("word_len_max")],
        *[pl.col("word_len").mean().alias("word_len_mean")],
        *[pl.col("word_len").min().alias("word_len_min")],
        #*[pl.col(fea).kurtosis().alias(f"{fea}_kurtosis") for fea in paragraph_fea],
        *[pl.col("word_len").quantile(0.25).alias("word_len_q1")],
        *[pl.col("word_len").quantile(0.5).alias("word_len_q2")],
        *[pl.col("word_len").quantile(0.75).alias("word_len_q3")]
        ]
    
    train = train.group_by(["essay_id"], maintain_order = True).agg(aggs)
    df = train.to_pandas()
    return df


def get_feats(para, sent, word):
    """Returns all Newly created Features"""
    feats = pd.merge(para, sent, how = "inner", on = "essay_id")
    feats = pd.merge(feats, word, how = "inner", on = "essay_id")
    return feats


def GET_ALL_FEATS(path, mode="train"):
    
    # Loading files
    train = pl.read_csv(path)
    tr = pd.read_csv(path)


    para_col = [pl.col(["full_text"]).str.split("\n\n").alias("paragraph")] 

    train = train.with_columns(para_col)
    train = train.with_columns(pl.col("full_text").map_elements(remove__, return_dtype = str).alias("full_text"))

    
    li = []
    lii = []
    for row in tr["full_text"]:
        j,_ = find_span_length(row)
        li.append(j)
        lii.append(_)

    ## SPAN FEATURES FOR FULL_TEXT 
    tr["length"] = tr["full_text"].apply(lambda x: len(re.sub("\s{2,100000}", " ", x)))
    tr["spans"] = li
    tr["spansN"] = lii
    tr["span%"] = tr["spans"]/ tr["length"]
    tr["spansAvg"] = tr["spans"]/tr["spansN"]
    
    # Paragraph Features
    para_df = ParaPreprocessing(train)
    para_df, cc = ParaFeatures(para_df)

    # Sentence Features
    sent_df = SentPreprocessing(train)
    sent_df = SentFeatures(sent_df)

    # Word Features
    word_df = WordPreprocessing(train)
    word_df = WordFeatures(word_df)
    
    feats = get_feats(para_df, sent = sent_df, word = word_df)

    ## Vectorizers
    cnt_n = CountVectorizer(min_df = .02, max_df = .97,ngram_range=(1,3),analyzer="char",
                #token_pattern=None,
                tokenizer=None,
                strip_accents = 'unicode',
                #preprocessor=lambda x: x,
                )
    
    cnt_n2 = CountVectorizer(min_df = .05, max_df = .95,ngram_range=(1,3),analyzer="word",
                #token_pattern=None,
                tokenizer=None,
                strip_accents = 'unicode',
                #preprocessor=lambda x: x,
                )
    
    # Fit vectorizers to the dataset for Training
    if mode!="predict":
        cnt_n.fit([i for i in train["full_text"]])
        cnt_n2.fit([i for i in train["full_text"]])
      
    # Load vectorizers to use transform feature
    if mode=="predict":
        cnt_n = pickle.load(open(SETTINGS["COUNT_VECTORIZER1_PATH"], "rb"))
        cnt_n2 = pickle.load(open(SETTINGS["COUNT_VECTORIZER2_PATH"], "rb"))
        
    
    tok_tff = cnt_n.transform([i for i in train["full_text"]])
    tok_tf = cnt_n2.transform([i for i in train["full_text"]])
    
    # Saving Vectorizers during Training mode
    if mode!="predict":
        pickle.dump(cnt_n, open(SETTINGS["COUNT_VECTORIZER1_PATH"], "wb"))
        pickle.dump(cnt_n2, open(SETTINGS["COUNT_VECTORIZER2_PATH"], "wb"))
    
    # Horizontally stacking all the features
    Feats = hstack((
        coo_matrix(feats.drop(columns = ["essay_id"], axis = 1)), 
        coo_matrix(tok_tf), 
        coo_matrix(tok_tff),
        coo_matrix(tr[["spans", "span%", "spansAvg"]]),
                    ))
    
    Feats = pd.DataFrame(Feats.toarray())
    Feats.to_csv(SETTINGS["CLEAN_DATA_PATH"], index = False)

if SETTINGS["GET_CLEAN_DATA"]:
    GET_ALL_FEATS(SETTINGS["SAMPLE_DATA_PATH"])
