# 📘 README.md

## Tata Motors: Alternative Data Technical Assessment

This repository presents a complete pipeline to use alternative macroeconomic indicators for predicting Tata Motors' financial performance. It is part of a technical assessment for Finance Club applications.

### Project Structure:

```
.
├── data/                        # Raw and intermediate CSVs
├── outputs/                     # Cleaned data + all plots (auto-saved)
├── notebooks/
│   ├── 01_data_cleaning.ipynb              
│   ├── 02_analysis_and_signals.ipynb       
│   ├── 03_modeling_and_prediction.ipynb    
│   └── 04_fundamental_validation.ipynb     
├── requirements.txt
├── README.md
└── CandidateName_TechnicalAssessment_Report.pdf
```

### Notebook Summary

- `01_data_cleaning.ipynb`
    - Loads and cleans simulated auto sales, CPI index, and repo rate data.
    - Merges all sources to monthly frequency and stores in `cleaned_macro_data.csv`.

- `02_analysis_and_signals.ipynb`
    - Creates predictive macro signals: Auto_YoY, CPI Acceleration, Repo Change.
    - Calculates correlation & Granger causality.
    - Saves `macro_signals.csv` + plots into outputs/.

- `03_modeling_and_prediction.ipynb`
    - Uses signals to predict simulated quarterly revenue.
    - Applies Linear Regression and evaluates R² + RMSE.
    - Saves prediction results and plots.

- `04_fundamental_validation.ipynb`
    - Predicts next-quarter profit margin using signals.
    - Aligns signal behavior with business fundamentals.


### Setup Instructions

1. Clone repo and install dependencies:
```bash
pip install -r requirements.txt
```

2. Run notebooks in order inside `notebooks/` folder.

3. Outputs (plots and CSVs) are auto-saved in the `outputs/` directory.

#### GitHub Repository
https://github.com/Vivek-Raju-02/tata-motors-altdata-prediction
