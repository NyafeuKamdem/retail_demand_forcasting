# retail_demand_forcasting

# Corporación Favorita Sales Forecasting App

## Purpose
This Streamlit app forecasts sales for the Guayas region using the best XGBoost model from Sprint 3. Demand planners can explore forecasts for specific stores and items, select a date range (Jan–Mar 2014), and visualize predictions alongside actual sales.

## Model Choice & Performance
- **Model:** XGBoost (fast, reliable, strong validation performance)
- **Metrics from Sprint 3:**
  - RMSE: <insert RMSE here>
  - MAE: <insert MAE here>
- The model was trained on historical sales data and engineered features to predict unit sales accurately.

## Project Structure
retail_demand_forcasting/
│
├── app/
│ ├── main.py # Streamlit app UI
│ ├── config.py # Paths and constants
│ ├── init.py
│ ├── tuned_xgb_model.pkl
│ ├── feature_columns.pkl
│ └── xbg_df.csv
│
├── data/
│ ├── data_utils.py
│ └── init.py
│
├── model/
│ ├── model_utils.py
│ └── init.py
│
├── mlflow_results/ # MLflow experiments (Colab)
├── requirements.txt
└── README.md


## Setup & Run Instructions
1. Clone the repository:

```bash
git clone <your_repo_link>
cd retail_demand_forcasting


2. Install dependencies:
pip install -r requirements.txt


3. Run the Streamlit app:
streamlit run app/main.py


4. In the app:

Select Store ID

Select Item (SKU)

Select Date range (Jan–Mar 2014)

Click Get Forecast to see predictions, metrics, and plots.


Notes
Only one store–SKU combination is included to keep the app fast and reliable.

MLflow tracking is only on Google Colab; no local MLflow setup is needed.

Ensure tuned_xgb_model.pkl, feature_columns.pkl, and xbg_df.csv are in the app/ folder.