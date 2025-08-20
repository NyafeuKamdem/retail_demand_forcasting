# app/main.py
import os
import joblib
import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt
from sklearn.metrics import mean_squared_error, mean_absolute_error
import numpy as np

# --- Base directory ---
BASE_DIR = os.path.dirname(__file__)  # folder containing main.py

# --- Load model, features, and dataset ---
model = joblib.load(os.path.join(BASE_DIR, "tuned_xgb_model.pkl"))
feature_columns = joblib.load(os.path.join(BASE_DIR, "feature_columns.pkl"))
data = pd.read_csv(os.path.join(BASE_DIR, "xbg_df.csv"))

# Ensure proper date format
data['date'] = pd.to_datetime(data['date'])

st.title("📈 Corporación Favorita Sales Forecasting")

# --- Store selection ---
store_nbr = st.selectbox("🏬 Select Store ID", data['store_nbr'].unique())
data_filtered = data[data['store_nbr'] == store_nbr]

# --- Item selection ---
item_nbr = st.selectbox("📦 Select Item ID", data_filtered['item_nbr'].unique())
data_filtered = data_filtered[data_filtered['item_nbr'] == item_nbr]


# --- Date filter (interactive) ---
import datetime

# Hardcoded date range for Jan–Mar 2014
min_date = datetime.date(2014, 1, 1)
max_date = datetime.date(2014, 3, 31)

# Streamlit slider
date_range = st.slider(
    "📅 Select Date Range",
    min_value=min_date,
    max_value=max_date,
    value=(min_date, max_date)
)

# Filter dataframe to stay within Jan–Mar 2014
data_filtered = data_filtered[
    (data_filtered['date'] >= pd.Timestamp(min_date)) &
    (data_filtered['date'] <= pd.Timestamp(max_date))
]


# --- Forecast button ---
if st.button("🔮 Get Forecast"):
    # Prepare features and make predictions
    X_input = data_filtered[feature_columns]
    prediction = model.predict(X_input)

    # Combine with actuals
    result_df = pd.DataFrame({
        "date": data_filtered['date'],
        "actual_sales": data_filtered['unit_sales'],
        "predicted_sales": prediction
    })

    st.write("✅ Forecast Results:", result_df.head())

    # --- Metrics ---
    rmse = np.sqrt(mean_squared_error(result_df['actual_sales'], result_df['predicted_sales']))
    mae = mean_absolute_error(result_df['actual_sales'], result_df['predicted_sales'])
    st.metric("RMSE", f"{rmse:.2f}")
    st.metric("MAE", f"{mae:.2f}")

    # --- Plot ---
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(result_df['date'], result_df['actual_sales'], label="Actual Sales", color="blue")
    ax.plot(result_df['date'], result_df['predicted_sales'], label="Predicted Sales", color="red")
    ax.set_xlabel("Date")
    ax.set_ylabel("Sales")
    ax.set_title(f"Sales Forecast for Store {store_nbr}, Item {item_nbr}")
    ax.legend()
    plt.xticks(rotation=45)
    st.pyplot(fig)

