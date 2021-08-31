# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 15:27:36 2021

@author: Admin
"""
import numpy
import pickle
import string
import re

lang_detect_file = open('D:/RICK/NLP INTERNSHIP/CODE/Code/ModelFile.pckl', 'rb')
lang_detect_model = pickle.load(lang_detect_file)
pun_dic = dict((ord(char), None) for char in string.punctuation)


def lang_detect(text):
    text = " ".join(text.split())
    text = text.lower()
    text = re.sub(r"\d+", "", text)
    text = text.translate(pun_dic)
    pred = lang_detect_model.predict([text])
    return pred[0]


lang_detect("Hello, how are you This is a beautiful day")
lang_detect("Hallo, wie geht es dir, das ist auf Deutsch")
lang_detect("हेलो कैसे हो आप, ये है हिंदी में")
lang_detect("नमस्कार कसे आहात, हे मराठीत आहे")
