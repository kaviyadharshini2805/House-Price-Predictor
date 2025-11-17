import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="House Price Predictor", layout="wide")

st.title("🏠 House Price Predictor")

# Load trained pipeline
pipeline = joblib.load("pipeline.pkl")

# Inputs list
features = [
    'bedrooms', 'bathrooms', 'sqft', 'lot_size', 'age', 'year_built',
    'garage', 'location', 'house_type', 'condition',
    'has_pool', 'has_fireplace', 'has_basement', 'school_rating'
]

inputs = {}

st.subheader("Enter House Details")

col1, col2 = st.columns(2)

for i, feature in enumerate(features):
    with col1 if i % 2 == 0 else col2:
        if feature in ['has_pool', 'has_fireplace', 'has_basement']:
            inputs[feature] = st.selectbox(feature, [0, 1])
        elif feature in ['location', 'house_type', 'condition']:
            inputs[feature] = st.text_input(feature)
        else:
            inputs[feature] = st.number_input(feature, step=1.0)

# Predict button
if st.button("Predict Price"):
    df_input = pd.DataFrame([inputs])
    prediction = pipeline.predict(df_input)[0]
    st.success(f"Predicted House Price: ₹{prediction:,.2f}")