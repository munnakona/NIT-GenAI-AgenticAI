# Advanced Statistics Project

This project demonstrates advanced statistical analysis on sales data for a retail store. It includes both a Jupyter Notebook for exploratory data analysis and a Streamlit web application for interactive visualization and analysis.

## Project Structure

- `Adv-Stats.ipynb`: Jupyter Notebook containing the complete statistical analysis workflow, including data generation, descriptive statistics, inferential statistics, and visualizations.
- `app.py`: Streamlit application providing an interactive web interface for the sales data analysis.
- `sales_data.csv`: Synthetic sales data generated for analysis (20 products across 4 categories).

## Features

### Descriptive Statistics
- Mean, median, mode, variance, and standard deviation of units sold
- Category-wise aggregation (total, average, and standard deviation)

### Inferential Statistics
- Confidence interval calculation for the mean units sold
- Hypothesis testing (t-test) to compare mean against a null hypothesis (μ = 20)

### Visualizations
- Histogram of units sold with mean, median, and mode lines
- Boxplot of units sold by category
- Bar plot of total units sold by category

## Dependencies

- Python 3.x
- pandas
- numpy
- scipy
- matplotlib
- seaborn
- streamlit

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/munnakona/Python_Basics.git
   cd Adv-Stats-Project
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Jupyter Notebook
Open `Adv-Stats.ipynb` in Jupyter Lab or Notebook and run all cells to perform the analysis.

### Streamlit App
Run the Streamlit application:
```bash
streamlit run app.py
```

Navigate to the provided localhost URL to interact with the analysis dashboard.

## Data

The project uses synthetic sales data generated using Poisson distribution for realistic sales patterns. The dataset includes:
- Product ID and name
- Product category (Electronics, Clothing, Home, Sports)
- Units sold
- Sale date

## Contributing

Feel free to fork this repository and submit pull requests with improvements or additional statistical analyses.

## License

This project is for educational purposes. Feel free to use and modify as needed.