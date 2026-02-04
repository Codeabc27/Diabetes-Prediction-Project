🩺 Diabetes Prediction ML Project

A Machine Learning web application that predicts whether a person has diabetes based on medical parameters.

This project is built using Python, Scikit-learn, Pandas, NumPy, and Flask and uses the PIMA Indians Diabetes Dataset.

📌 Project Overview

Diabetes is a serious health condition that affects millions of people worldwide. Early detection helps in proper treatment and prevention.

This project uses a trained Machine Learning classification model to predict whether a person is diabetic or not based on input health features.

🚀 Features

Data Cleaning & Preprocessing

Exploratory Data Analysis (EDA)

Machine Learning Model Training

Model Evaluation (Accuracy, Confusion Matrix, etc.)

Model saved using Joblib

Simple and user-friendly web interface

📊 Dataset Information

The dataset used: PIMA Indians Diabetes Dataset

🔹 Input Features:

Pregnancies

Glucose

Blood Pressure

Skin Thickness

Insulin

BMI

Diabetes Pedigree Function

Age

🎯 Target:

0 → Non-Diabetic

1 → Diabetic

🧠 Machine Learning Algorithms Used

Logistic Regression

Random Forest Classifier

Decision Tree

Support Vector Machine

The best-performing model is selected based on accuracy.

📂 Project Structure
Diabetes-Prediction-ML-Project/
│
├── data/
│   └── diabetes.csv
│
├── model/
│   └── diabetes_model.joblib
│
├── templates/
│   └── index.html
│
├── app.py
├── train_model.py
├── requirements.txt
└── README.md

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/Codeabc27/Diabetes-Prediction-ML-Project.git
cd Diabetes-Prediction-ML-Project

2️⃣ Create Virtual Environment
python -m venv venv


Activate it:

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Run the Application
python app.py


Open your browser and go to:

http://127.0.0.1:5000/

📈 Model Training

To retrain the model:

python train_model.py


The trained model will be saved inside:

model/diabetes_model.joblib

📊 Model Evaluation Metrics

Accuracy Score

Confusion Matrix

Precision

Recall

F1 Score

🛠 Technologies Used

Python

Pandas

NumPy

Matplotlib / Seaborn

Scikit-learn

Flask

Joblib

🔮 Future Improvements

Deploy to Render / AWS / Heroku

Improve UI design

Add model comparison dashboard

Add REST API support

Improve prediction accuracy

👨‍💻 Author

deadpool
GitHub: https://github.com/Codeabc27