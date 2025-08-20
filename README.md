# retail_demand_forcasting

# Corporación Favorita Sales Forecasting App

## Purpose
This Streamlit app forecasts sales for the Guayas region using the best XGBoost model from Sprint 3. Demand planners can explore forecasts for specific stores and items, select a date range (Jan–Mar 2014), and visualize predictions alongside actual sales.

## Model Choice & Performance
- **Model:** XGBoost (fast, reliable, strong validation performance)
- **Metrics from Sprint 3:**
  - RMSE: 3.653
  - MAE: 0.758
- The model was trained on historical sales data and engineered features to predict unit sales accurately.

## Project Structure
retail_demand_forcasting/
│
├── app/
│ ├── main.py # Streamlit app UI
│ ├── config.py # Paths and constants
│ ├── __init__.py
│ ├── tuned_xgb_model.pkl
│ ├── feature_columns.pkl
│ └── xbg_df.csv
│
├── data/
│ ├── data_utils.py
│ └── __init__.py
│
├── model/
│ ├── model_utils.py
│ └── __init__.py
│
├── mlflow_results/ # MLflow experiments (Colab)
├── requirements.txt
└── README.md


## Setup & Run Instructions
1. Clone the repository:

```
git clone https://github.com/NyafeuKamdem/retail_demand_forcasting
cd retail_demand_forcasting
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Place the dataset locally:

Download xbg_df.csv (108 MB) separately and save it in:
````
/Users/pnyaf/Documents/Datasets/xbg_df.csv
````
Then, in app/main.py, ensure the data path matches:
data = pd.read_csv("/Users/pnyaf/Documents/Datasets/xbg_df.csv")


4. Run the Streamlit app:

```
streamlit run app/main.py
```


5. In the app:

Select Store ID

Select Item (SKU)

Select Date range (Jan–Mar 2014)

Click Get Forecast to see predictions, metrics, and plots.


## Notes
- Only one store–SKU combination is included to keep the app fast and reliable.  
- MLflow tracking is only on Google Colab; no local MLflow setup is needed.  
- tuned_xgb_model.pkl, feature_columns.pkl, and xbg_df.csv are required for the app. The CSV is not in GitHub due to its size.

