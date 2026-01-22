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

# Bias
bias = regressor.score(x_train,y_train)

print(bias)


# Varience

variance = regressor.score(x_test, y_test)
print(variance)

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Predictions
y_train_pred = regressor.predict(x_train)
y_test_pred = regressor.predict(x_test)

# R2 Scores
train_r2 = r2_score(y_train, y_train_pred)
test_r2 = r2_score(y_test, y_test_pred)

# MSE
train_mse = mean_squared_error(y_train, y_train_pred)
test_mse = mean_squared_error(y_test, y_test_pred)

# RMSE
train_rmse = np.sqrt(train_mse)
test_rmse = np.sqrt(test_mse)

# MAE
train_mae = mean_absolute_error(y_train, y_train_pred)
test_mae = mean_absolute_error(y_test, y_test_pred)

# Output
print(f"Training R² Score: {train_r2:.2f}")
print(f"Testing R² Score: {test_r2:.2f}")
print(f"Training MSE: {train_mse:.2f}")
print(f"Testing MSE: {test_mse:.2f}")
print(f"Training RMSE: {train_rmse:.2f}")
print(f"Testing RMSE: {test_rmse:.2f}")
print(f"Training MAE: {train_mae:.2f}")
print(f"Testing MAE: {test_mae:.2f}")


# Save the Tained Mode
import pickle

filename = 'Linear_regression_model.pkl'

with open(filename,'wb')as file:
    pickle.dump(regressor, file)

print("Model has been pickled and savd as Linear_regression_model")

import os
print(os.getcwd())













