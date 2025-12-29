import streamlit as st
import numpy as np
import pickle

# -----------------------------------
# LOAD TRAINED MODEL
# -----------------------------------
model = pickle.load(open("final_taxi_fare_model.pkl", "rb"))

# -----------------------------------
# STREAMLIT PAGE CONFIG
# -----------------------------------
st.set_page_config(
    page_title="TripFare – Taxi Fare Prediction",
    page_icon="🚕",
    layout="centered"
)

# -----------------------------------
# APP TITLE
# -----------------------------------
st.title("🚕 TripFare – Taxi Fare Prediction")
st.markdown("Predict **total taxi fare** using a Machine Learning model")

st.divider()

# -----------------------------------
# USER INPUTS
# -----------------------------------
st.subheader("Enter Trip Details")

passenger_count = st.number_input(
    "Passenger Count",
    min_value=1,
    max_value=6,
    value=1
)

trip_duration_min = st.number_input(
    "Trip Duration (minutes)",
    min_value=1.0,
    value=10.0
)

pickup_hour = st.slider(
    "Pickup Hour (0–23)",
    min_value=0,
    max_value=23,
    value=12
)

is_weekend = st.selectbox(
    "Is it a Weekend?",
    options=[0, 1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

is_night = st.selectbox(
    "Is it a Night Ride?",
    options=[0, 1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)

# -----------------------------------
# PREDICTION
# -----------------------------------
if st.button("Predict Fare 💰"):

    # IMPORTANT: Feature order MUST match training order
    input_data = np.array([[
        passenger_count,
        trip_duration_min,
        pickup_hour,
        is_weekend,
        is_night
    ]])

    prediction = model.predict(input_data)[0]

    st.success(f"Estimated Total Fare: **${prediction:.2f}**")

# -----------------------------------
# FOOTER
# -----------------------------------
st.caption("TripFare | Machine Learning Taxi Fare Prediction App")
