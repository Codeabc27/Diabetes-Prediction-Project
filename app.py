from flask import Flask, render_template, request
import joblib
import numpy as np
import os

# Load trained model
MODEL_PATH = os.path.join(
    os.path.dirname(__file__), "model", "logistic_regression_diabetes_model.joblib"
)
try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    # Fail fast with a clear message so developer can fix the path or reinstall dependencies
    raise RuntimeError(f"Failed to load model from '{MODEL_PATH}': {e}")

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
