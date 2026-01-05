# LLM-Powered Exploratory Data Analysis (EDA) App

This is a web-based application built with Gradio that performs automated Exploratory Data Analysis (EDA) on uploaded CSV datasets. It leverages AI (via Ollama's Gemma3 model) to generate insights and creates visualizations for better data understanding.

## Features

- **Automated Data Loading and Preprocessing**: Loads CSV files and handles missing values (median for numeric, mode for categorical).
- **Data Summary**: Generates descriptive statistics for all columns.
- **Missing Values Report**: Identifies and reports missing data.
- **AI-Powered Insights**: Uses LLM (Gemma3:270m via Ollama) to analyze the dataset and provide intelligent insights.
- **Data Visualizations**: Automatically generates:
  - Histograms for all numeric columns with KDE plots.
  - Correlation heatmap for numeric variables.
- **Interactive Web Interface**: Easy-to-use Gradio interface for uploading files and viewing results.

## Requirements

- Python 3.7+
- Required Python packages:
  - gradio
  - pandas
  - matplotlib
  - seaborn
  - ollama

Install dependencies using pip:
```
pip install gradio pandas matplotlib seaborn ollama
```

## Prerequisites

- **Ollama**: Must be installed and running locally. Download from [ollama.ai](https://ollama.ai).
- **Gemma3 Model**: Pull the model before running:
  ```
  ollama pull gemma3:270m
  ```

## How to Run

1. Ensure Ollama is running in the background.
2. Navigate to the directory containing `app.py`.
3. Run the application:
   ```
   python app.py
   ```
4. The app will launch in your default web browser with a public shareable link (if `share=True`).

## Usage

1. Upload a CSV file using the file input.
2. The app will process the data and display:
   - A text report with data summary, missing values, and AI insights.
   - A gallery of generated visualizations (histograms and heatmap).
3. Visualizations are saved as PNG files in the current directory.

## Notes

- The app fills missing values automatically during preprocessing.
- Generated plots are saved locally and displayed in the interface.
- Ensure your CSV file has proper headers for best results.
- The AI insights are generated based on the dataset summary and may vary.

## Troubleshooting

- If Ollama is not running, the AI insights generation will fail.
- Large datasets may take longer to process.
- Ensure all required packages are installed.

## License

This project is for educational purposes. Modify and distribute as needed.
