from flask import Flask, render_template, request
import joblib
import numpy as np

# Load trained model
model = joblib.load("logistic_regression_diabetes_model.joblib")

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        features = [float(x) for x in request.form.values()]
        final_input = np.array([features])
        prediction = model.predict(final_input)[0]

        result = "Diabetes" if prediction == 1 else "No Diabetes"
        return render_template("index.html", prediction_text=f"Prediction: {result}")

    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {e}")


if __name__ == "__main__":
    app.run(debug=True)
