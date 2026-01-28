#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 15:22:32 2026

@author: munna
"""

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt


dataset = pd.read_csv(r"/Users/munna/VScode/NareshIT/Logistic Regression/logit classification.csv")


X = dataset.iloc[:,[2,3]].values


y = dataset.iloc[:, -1].values



from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.20, random_state=0)



#Fitting Logistics regression to the Training Set
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


#Logistics Regression Model

from sklearn.linear_model import LogisticRegression

Classifier = LogisticRegression()

Classifier.fit(X_train, y_train)


y_pred = Classifier.predict(X_test)



# Confusion Matrix

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test,y_pred)

print(cm)

# Accuracy of the Model

from sklearn.metrics import accuracy_score

ac = accuracy_score(y_test,y_pred)
print(ac)



from sklearn.metrics import classification_report

cr = classification_report(y_test, y_pred)
print(cr)



bias = Classifier.score(X_train, y_train)
print(bias)

variance = Classifier.score(X_test, y_test)
print(variance)






















































