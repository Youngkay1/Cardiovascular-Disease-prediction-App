# app.py
import streamlit as st
import pandas as pd
import joblib

# Load the saved model
model = joblib.load("best_model_lr.pkl")

st.title("Cardiovascular Disease Prediction App")
st.write("Fill in the patient details below to predict the risk of cardiovascular disease.")

st.markdown("""
    <style>
    footer {visibility: hidden;}
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        text-align: center;
        padding: 10px;
        font-size: 14px;
        color: gray;
    }
    </style>
    <div class="footer">
        © 2025 Cardiovascular Disease Prediction App <br>
        This is a statistical prediction and not a medical diagnosis.
    </div>
    """, unsafe_allow_html=True)


# Input Features
age = st.number_input("Age (years)", min_value=1, max_value=120, value=50)
gender = st.selectbox("Gender", options=[1, 2], format_func=lambda x: "Female" if x == 1 else "Male")
height = st.number_input("Height (cm)", min_value=50, max_value=250, value=170)
weight = st.number_input("Weight (kg)", min_value=10.0, max_value=300.0, value=70.0)
ap_hi = st.number_input("Systolic Blood Pressure (ap_hi)", min_value=50, max_value=250, value=120)
ap_lo = st.number_input("Diastolic Blood Pressure (ap_lo)", min_value=30, max_value=200, value=80)
cholesterol = st.selectbox("Cholesterol Level", options=[1, 2, 3], format_func=lambda x: ["Normal", "Above Normal", "Well Above Normal"][x-1])
gluc = st.selectbox("Glucose Level", options=[1, 2, 3], format_func=lambda x: ["Normal", "Above Normal", "Well Above Normal"][x-1])
smoke = st.selectbox("Smoking Status", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
alco = st.selectbox("Alcohol Intake", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
active = st.selectbox("Physical Activity", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")

# Automatically calculate BMI
bmi = round(weight / ((height / 100) ** 2), 2)
st.write(f"**Calculated BMI:** {bmi}")

# -------------------------------
# Prepare Input for Model
# -------------------------------
features = pd.DataFrame([[
    age, gender, height, weight, ap_hi, ap_lo, cholesterol,
    gluc, smoke, alco, active, bmi
]], columns=["age","gender","height","weight","ap_hi","ap_lo","cholesterol",
             "gluc","smoke","alco","active","bmi"])

# Prediction

if st.button("🔍 Predict"):
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]  # Probability of class 1 (cardio)

    if prediction == 1:
        st.warning(f"⚠️ The patient may be **at risk** of cardiovascular disease "
                   f"(Estimated Risk Probability: {probability*100:.2f}%).")
    else:
        st.info(f"✅ The patient is likely **not at risk** of cardiovascular disease "
                f"(Estimated Health Probability: {(1-probability)*100:.2f}%).")

        
    st.write("**Note:** This prediction is based on a machine learning model and should not replace professional medical advice.")
    st.write("Please consult a healthcare professional for a comprehensive evaluation.")

    
    
