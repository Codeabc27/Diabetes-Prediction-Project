import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import os

file_path = os.path.join(os.path.dirname(__file__), "diabetes.csv")

df = pd.read_csv(file_path)

print("Dataset loaded successfully. Displaying the first 5 rows:")
print(df.head())

X = df.drop("Outcome", axis=1)
y = df["Outcome"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Training set size: {X_train.shape[0]} samples")
print(f"Testing set size: {X_test.shape[0]} samples")

model = LogisticRegression(max_iter=200, random_state=42)
model.fit(X_train, y_train)

print("Logistic Regression model trained successfully.")

y_pred = model.predict(X_test)

print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

model_filename = "logistic_regression_diabetes_model.joblib"
joblib.dump(model, model_filename)

print(f"Model successfully exported as '{model_filename}'") # Current working directory