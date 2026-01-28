#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 26 15:32:37 2026

@author: munna
"""

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

dataset = pd.read_csv(r"/Users/munna/VScode/NareshIT/Polynomial_Technique/emp_sal.csv")


X = dataset.iloc[:,1:2].values

y = dataset.iloc[:,2].values

from sklearn.linear_model import LinearRegression

lin_reg = LinearRegression()
lin_reg.fit(X, y)



plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg.predict(X),color= 'blue')
plt.title('Linear Regression Graph')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()




lin_model_pred = lin_reg.predict([[6.5]])
lin_model_pred


from sklearn.preprocessing import PolynomialFeatures

poly_reg = PolynomialFeatures()
X_poly = poly_reg.fit_transform(X)
poly_reg.fit(X_poly,y)


lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)



plt.scatter(X, y, color = 'red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)),color= 'blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()



# Prediction

poly_model_pred = lin_reg_2.predict(poly_reg.fit_transform(X))

lin_model_pred = lin_reg.predict([[6.5]])
lin_model_pred

poly_model_pred = lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))
poly_model_pred



# SVR Model

from sklearn.svm import SVR

svr_reg = SVR(kernel='poly',degree=5)
svr_reg.fit(X, y)

svr_model_pred = svr_reg.predict([[6.5]])
svr_model_pred


# KNN Model

from sklearn.neighbors import KNeighborsRegressor


knn_reg = KNeighborsRegressor(n_neighbors=4)
knn_reg.fit(X, y)

knn_model_pred = knn_reg.predict([[6.5]])
knn_model_pred


# DTR Model

from sklearn.tree import DecisionTreeRegressor


dt_reg = DecisionTreeRegressor()
dt_reg.fit(X, y)


dt_model_pred = dt_reg.predict([[6.5]])
dt_model_pred





# RFR  Model

from sklearn.ensemble import RandomForestRegressor


rfr_reg = RandomForestRegressor()
rfr_reg.fit(X, y)


rfr_model_pred = rfr_reg.predict([[6.5]])
rfr_model_pred
























