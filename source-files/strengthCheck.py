import pandas as pd
import numpy as np
import random

from scipy.special import logit
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier


data = pd.read_csv("data/training-data.csv", on_bad_lines='skip')
data.dropna(inplace=True)

pswd = np.array(data)

#shuffle date for model to not remember patterns in database

random.shuffle(pswd)

#features and labels (features are our train data -> passwords)

ylabels  = [s[1] for s in pswd]
allpasswords = [s[0] for s in pswd]

#tokenizations bcs NN cant work with words

def createTokens(f):
    tokens = []
    for i in f:
        tokens.append(i)
    return tokens

vectorizer = TfidfVectorizer(tokenizer=createTokens)
X = vectorizer.fit_transform(allpasswords)

#80% of data used for training and 20% for testing

X_train, X_test, y_train, y_test = train_test_split(X, ylabels, test_size=0.2, random_state=42)

#model
clf=DecisionTreeClassifier()
clf.fit(X_train, y_train)


def passStrength(passString):
    X_predict = []
    X_predict.append(passString)

    X_predict = vectorizer.transform(X_predict)
    y_Predict = clf.predict(X_predict)
    return y_Predict
