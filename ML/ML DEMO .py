# Import necessary libraries for data manipulation, numerical operations, and plotting
import numpy as np  # NumPy for numerical operations and array handling
import pandas as pd  # Pandas for data manipulation and analysis
import matplotlib.pyplot as plt  # Matplotlib for plotting (though not used in this script)

# Load the dataset from a CSV file located at the specified path
dataset = pd.read_csv(r"/Users/munna/VScode/NareshIT/ML/Data.csv")

# Extract features (independent variables) from the dataset, excluding the last column
x = dataset.iloc[:, :-1].values
# Extract the target variable (dependent variable) from the last column (index 3)
y = dataset.iloc[:, 3].values

# Import SimpleImputer from sklearn for handling missing values
from sklearn.impute import SimpleImputer

# Create an imputer instance that replaces missing values with the most frequent value in each column
imputer = SimpleImputer(strategy="most_frequent")

# Fit the imputer on the specified columns (1 and 2) of x
imputer = imputer.fit(x[:, 1:3])

# Transform the specified columns (1 and 2) of x using the fitted imputer
x[:, 1:3] = imputer.transform(x[:, 1:3])

# Import LabelEncoder from sklearn for encoding categorical variables
from sklearn.preprocessing import LabelEncoder

# Create a LabelEncoder instance for the first column of x
LabelEncoder_x = LabelEncoder()

# Fit and transform the first column of x (categorical to numerical)
x[:,0] = LabelEncoder_x.fit_transform(x[:,0])

# Create another LabelEncoder instance for the target variable y
LabelEncoder_y = LabelEncoder()

# Fit and transform the target variable y (categorical to numerical)
y = LabelEncoder_y.fit_transform(y)

# Import train_test_split from sklearn for splitting the dataset
from sklearn.model_selection import train_test_split

# Split the dataset into training and testing sets with 80% training and 20% testing, random state for reproducibility
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,train_size=0.8,random_state=0)
