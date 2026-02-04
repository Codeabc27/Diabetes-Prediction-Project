# Diabetes Prediction Web App 🔬

**Simple, lightweight web app** that predicts diabetes using a trained logistic regression model. Built with **Flask** and scikit-learn, the app provides a minimal UI for entering patient features and getting a prediction.

---

## Features ✅

- Web form for entering 8 clinical features (Pregnancies, Glucose, Blood Pressure, Skin Thickness, Insulin, BMI, Diabetes Pedigree Function, Age)
- Uses a pre-trained Logistic Regression model (`logistic_regression_diabetes_model.joblib`)
- Easy to retrain using `model/logistic_model.py` and the included dataset

---

## Quick Start 🔧

1. Create and activate a virtual environment:

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

2. Install dependencies (from `pyproject.toml`):

```bash
pip install -e .
# or install required packages directly
pip install flask joblib numpy pandas scikit-learn pyngrok
```

3. Run the app:

```bash
python app.py
```

Open http://127.0.0.1:5000 in your browser and use the form to get predictions.

---

## Retraining the model 💾

To retrain using the provided dataset (`data/diabetes.csv`):

```bash
python model/logistic_model.py
```

The script trains a Logistic Regression model, prints evaluation metrics, and exports the model as `logistic_regression_diabetes_model.joblib`.

Note: the training script expects to find the CSV at `model/data/diabetes.csv` relative to the script; if running from the project root, ensure the file path is correct or adjust the script accordingly.

---

## Project Structure 📁

- `app.py` — Flask application
- `model/logistic_model.py` — training script
- `logistic_regression_diabetes_model.joblib` — trained model
- `templates/index.html` — web UI
- `data/diabetes.csv` — dataset (Pima Indians Diabetes)

---

## Input fields (form) 📝

- `pregnancies`, `glucose`, `bloodpressure`, `skinthickness`, `insulin`, `bmi`, `dpf`, `age`

These are submitted via the web form to `/predict` and returned as `Prediction: Diabetes` or `Prediction: No Diabetes`.

---

## License & Contributing 🤝

This project is provided as-is for learning and demo purposes. Contributions, fixes, and improvements are welcome — please open an issue or a pull request.

---

**Happy testing!**  ✨
