# ML Demo Project

This project demonstrates basic machine learning data preprocessing techniques using Python and scikit-learn.

## Overview

The `ML DEMO .py` script performs the following preprocessing steps on a dataset loaded from `Data.csv`:

1. **Data Loading**: Loads the dataset using pandas.
2. **Feature Extraction**: Separates features (X) and target variable (y).
3. **Missing Value Imputation**: Uses SimpleImputer to fill missing values with the most frequent value in columns 1 and 2.
4. **Label Encoding**: Converts categorical variables to numerical using LabelEncoder for both features and target.
5. **Train-Test Split**: Splits the data into training and testing sets (80% train, 20% test) using train_test_split.

## Dependencies

- numpy
- pandas
- scikit-learn
- matplotlib (imported but not used in this script)

## Usage

1. Ensure `Data.csv` is in the same directory as the script.
2. Run the script: `python "ML DEMO .py"`
3. The script will preprocess the data and create training and testing sets.

## File Structure

- `ML DEMO .py`: Main preprocessing script
- `Data.csv`: Input dataset
- `README.md`: This file

## Notes

- The dataset path is hardcoded; update as needed.
- Matplotlib is imported but not utilized in the current script.
- Random state is set to 0 for reproducibility.
