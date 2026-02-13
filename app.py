import streamlit as st
import pandas as pd
import pickle
import os
import json
from PIL import Image

with open("crop_model_optimized.pkl", "rb") as file:
    model = pickle.load(file)

if os.path.exists("crop_info.json"):
    with open("crop_info.json", "r") as file:
        crop_info = json.load(file)
else:
    crop_info = {}


st.set_page_config(page_title="Crop Recommendation", layout="wide")
st.markdown("<h1 style='text-align: center;'>🌾 Smart Crop Recommendation System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter soil and weather conditions to get the best crop suggestion.</p>", unsafe_allow_html=True)

st.markdown("---")

left_col, right_col = st.columns([1, 1])

with left_col:
    st.subheader("Input Parameters")
    N = st.number_input("Nitrogen content (N)", 0.0, 150.0, step=1.0)
    P = st.number_input("Phosphorus content (P)", 0.0, 150.0, step=1.0)
    K = st.number_input("Potassium content (K)", 0.0, 200.0, step=1.0)
    temperature = st.number_input("Temperature (°C)", 0.0, 50.0, step=0.1)
    humidity = st.number_input("Humidity (%)", 0.0, 100.0, step=0.1)
    ph = st.number_input("pH value", 0.0, 14.0, step=0.1)
    rainfall = st.number_input("Rainfall (mm)", 0.0, 300.0, step=1.0)

    if st.button("🔍 Predict Crop"):
        input_data = [[N, P, K, temperature, humidity, ph, rainfall]]
        prediction = model.predict(input_data)[0]

        st.session_state.prediction = prediction

if "prediction" in st.session_state:
    prediction = st.session_state.prediction
    with right_col:
        st.subheader("🌟 Recommended Crop")
        st.success(f"**{prediction.title()}**")

        image_path = f"images/{prediction}.png"
        if os.path.exists(image_path):
            img = Image.open(image_path)
            img = img.resize((360, 360))
            st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
            st.image(img, caption=prediction.title(), use_container_width=False)
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.info("📷 Crop image not available.")

        if prediction in crop_info:
            st.markdown("### 🌿 Crop Details")
            st.markdown(f"**🌦️ Climate:** {crop_info[prediction]['climate']}")
            st.markdown(f"**📌 Tip:** {crop_info[prediction]['tip']}")
        else:
            st.info("ℹ️ No additional info available for this crop.")


