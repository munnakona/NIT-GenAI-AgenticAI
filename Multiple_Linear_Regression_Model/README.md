# Multiple Linear Regression Model

## Description

This project demonstrates the implementation of a multiple linear regression model using Python. The model is trained on investment data to predict outcomes based on various features. The implementation includes data preprocessing, model training, prediction, and evaluation using Ordinary Least Squares (OLS) for feature selection.

## Dataset

The dataset used is `Investment.csv`, which contains investment-related features. The target variable is in the 5th column (index 4), and the predictor variables are the preceding columns.

## Features

- Data loading and preprocessing using pandas
- Dummy variable encoding for categorical features
- Train-test split for model evaluation
- Linear regression model training with scikit-learn
- Prediction on test data
- OLS regression with statsmodels for feature selection (backward elimination)
- Model evaluation metrics (bias and variance)

## Dependencies

The following Python packages are required:

- numpy
- pandas
- matplotlib
- scikit-learn
- statsmodels

## Installation

Install the required packages using pip:

```bash
pip install numpy pandas matplotlib scikit-learn statsmodels
```

## Usage

1. Ensure the `Investment.csv` file is in the same directory as the script.
2. Run the Python script:

```bash
python Multiple_Linear_Regression_Model.py
```

The script will:
- Load and preprocess the data
- Train the linear regression model
- Print the model coefficients and intercept
- Perform OLS regression and feature selection
- Calculate and display bias (training score) and variance (test score)

## Output

The script prints:
- Model coefficients (slopes for each feature)
- Model intercept
- OLS regression summaries (for feature selection steps)
- Training score (bias)
- Test score (variance)

## Notes

- The script uses a hardcoded path for the CSV file. Modify the path in the script if needed.
- The random state is set to 0 for reproducibility.
- The test size is 1/3 of the dataset.

## License

This project is for educational purposes.