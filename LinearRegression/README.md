# Linear Regression Project

This project demonstrates a simple linear regression model to predict salaries based on years of experience using Python and scikit-learn.

## Files

- `simple_linear_regression.py`: Python script that implements the linear regression model.
- `Salary_Data.csv`: Dataset containing salary and experience data.

## Requirements

- Python 3.x
- NumPy
- Pandas
- Matplotlib
- Scikit-learn

## Installation

Install the required packages using pip:

```
pip install numpy pandas matplotlib scikit-learn
```

## Usage

Run the script from the command line:

```
python simple_linear_regression.py
```

The script will:
- Load the dataset
- Split the data into training and testing sets
- Train a linear regression model
- Make predictions on the test set
- Display a comparison of actual vs predicted values
- Plot the regression line
- Print the slope, intercept, and predicted salaries for 15 and 20 years of experience

## Output

- Console output showing actual vs predicted salaries
- Scatter plot with regression line
- Model coefficients (slope and intercept)
- Predicted salaries for specific experience levels
