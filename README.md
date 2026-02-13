# Crop-Recommendation-System-
Machine Learning based crop recommedation system that predicts the crop based on the soil and climatic condition.
📌 Project Overview
This Crop Recommendation System uses Machine Learning to help farmers and agricultural planners choose the most suitable crop to cultivate based on inputs like nitrogen, phosphorus, potassium, temperature, humidity, pH, and rainfall.

🔗 Live App: https://crop-predictor-system.streamlit.app/
📊 Dataset: https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset
🧠 Features
Takes 7 environmental inputs (N, P, K, temperature, humidity, pH, rainfall)

Predicts from 22 crops (like Rice, Wheat, Tea, Cotton, etc.)

Shows crop image, ideal climate, and growing tips

Clean and responsive Streamlit UI

🛠️ Tools & Technologies Used
Python 🐍

Machine Learning (Random Forest Classifier)

Streamlit (for UI and deployment)

Pandas, NumPy, Scikit-learn

Matplotlib & Seaborn (for visualization)

PIL (for image handling)

🗂️ Project Structure
├── app.py # Streamlit web app
├── train_model.py # Model training script
├── crop_model_optimized.pkl # Trained ML model
├── crop_info.json # Crop tips and climate info
├── images/ # Crop images folder
├── requirements.txt # Python dependencies
└── README.md # This file

📈 Model Details
Algorithm: Random Forest Classifier

Accuracy: ~99.3%

Trained on: 2200+ samples with 22 crop labels

Evaluation: Confusion matrix, classification report, accuracy score

🔍 Sample Input
Parameter	Value
Nitrogen (N)	90
Phosphorus (P)	42
Potassium (K)	43
Temperature	25.5°C
Humidity	80.0%
pH	6.5
Rainfall	100 mm
🟢 Output: Recommended Crop → Jute / Rice / etc. (based on prediction)
🚀 How to Run Locally
1. Clone the repo:
git clone https://github.com/aayush2004-hack/Crop-Recommendation-System.git
cd Crop-Recommendation-System

2. Install dependencies:
pip install -r requirements.txt

3. Run the app:
streamlit run app.py

🌍 Deployment
Deployed via Streamlit Cloud Simply pushed to GitHub and linked with Streamlit’s deployment platform.

👨‍💻 Authors
Aayush Sharma
Aditya Choudhary
Himanshu Yadav
Nitesh Kumar
