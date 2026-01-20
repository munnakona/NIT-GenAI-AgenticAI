#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 15:48:40 2026

@author: munna
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


dataset = pd.read_csv(r"/Users/munna/VScode/NareshIT/LinearRegression/Salary_Data.csv")

x = dataset.iloc[:,:-1].values

y = dataset.iloc[:,-1].values


from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.20, random_state=0)


from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)


comparison = pd.DataFrame({'Actual': y_test,'Predicted':y_pred})

print(comparison)

plt.scatter(x_test,y_test,color = 'red')
plt.plot(x_train,regressor.predict(x_train),color='blue')
plt.title('Salary vs Experience (Test Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()


m_slope = regressor.coef_

print(m_slope)

C_intercept = regressor.intercept_
print(C_intercept)

emp_15 = m_slope* 15 +  C_intercept

print(emp_15)


emp_20 = m_slope* 20 +  C_intercept

print(emp_20)























