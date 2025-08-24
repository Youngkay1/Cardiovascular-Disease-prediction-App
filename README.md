# Cardiovascular-Disease-prediction-App

This project is a Streamlit web application for predictive analysis of cardiovascular diseases. It uses Logistic Regression as the final model after evaluating multiple classifiers. The app provides an interpretable probability score along with predictions (Healthy / At Risk).

Features

Exploratory Data Analysis (EDA) with visual insights

Data preprocessing (handling outliers, BMI calculation, cleaning blood pressure values)

Model training and evaluation with metrics (Accuracy, Precision, Recall, F1, AUC-ROC)

Final model selection (Logistic Regression)

Deployment-ready Streamlit application for real-time prediction

Dataset

The dataset was obtained from Kaggle:
Cardiovascular Disease dataset – Sulianova

Rows: 70,000 patient records

Target variable: cardio (0 = No Cardiovascular Disease, 1 = Cardiovascular Disease)

Features: Age, Gender, Height, Weight, Blood Pressure (ap_hi, ap_lo), Cholesterol, Glucose, Smoking, Alcohol, Physical Activity, BMI

Installation & Usage

Clone this repository:

git clone https://github.com/your-username/cardio-predict.git
cd cardio-predict


Install dependencies:

pip install -r requirements.txt


Run the Streamlit app:

streamlit run app.py

Deployment

The app can be deployed easily on Streamlit Community Cloud
.

Results

Logistic Regression achieved the best performance with:

Logistic Regression:
Accuracy: 0.73
Precision: 0.75
Recall: 0.66
F1 Score: 0.70
AUC-ROC: 0.79

AUC-ROC: 0.80

License

This project is for educational and research purposes only.
