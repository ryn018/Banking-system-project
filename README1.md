# Loan Amount Prediction Tool

This project builds a machine learning pipeline to predict the maximum loan amount a customer may be eligible for, based on their financial and personal profile. It can be used as part of a banking web application backend or as a standalone service.

---

## Problem Statement

Users want to estimate the loan amount they can receive from a bank, based on:

- Age
- Monthly Income
- Credit Score
- Loan Tenure (in years)
- Existing Loan Amount
- Number of Dependents

---

## Solution Overview

- A regression model (Random Forest) is trained using labeled financial data.
- Scikit-learn is used for preprocessing, training, and evaluation.
- The trained model and scaler are saved using "joblib".
- A prediction API lets users get estimates using new input values.
- The project includes unit tests using Python's "unittest" framework.

---

##  Project Structure
loan_amount_prediction/ 
├── loan_predictor.py # Main training pipeline (EDA, training, saving) 
├── predictor_api.py # Prediction logic using trained model 
├── test_loan_predictor.py # Unit tests for prediction and training 
├── loan_amount_prediction_dataset_v2.csv # Input dataset 
├── loan_model.pkl # Trained model (auto-generated) 
├── scaler.pkl # Preprocessing scaler (auto-generated) 
└── README.md # Documentation


 Features

-  Train a model with structured financial data
-  Predict loan amount from user input
-  Save and reuse trained model for real-time prediction
-  Built-in unit tests to verify functionality

---

## 🧪 Dataset Features

The model uses the following inputs (features):

| Feature Name             | Description                        |
|--------------------------|------------------------------------|
| `Age`                    | Applicant's age in years           |
| `Monthly_Income`         | Monthly salary or income in ₹      |
| `Credit_Score`           | Score from 300–850                 |
| `Loan_Tenure_Years`      | Number of years for the loan       |
| `Existing_Loan_Amount`   | Any current outstanding loan       |
| `Num_of_Dependents`      | Number of dependents in the family |
| `Loan_Amount`            |  (Target) Approved loan amount     |

---

##  Set Up

### Step 1: Install Dependencies

Run command:
pip install pandas numpy scikit-learn joblib

### Step 2 : Train the Model : saves the model + scaler

Run Command: 
python -c "import loan_predictor; loan_predictor.run_pipeline('loan_amount_prediction_dataset_v2.csv')"

### Step 3: Predication
Run Command: 
python run_prediction.py

### Step 4: Run Unit Tests
Run Command: 
python test_loan_predictor.py


### Technologies Used
Python 3.x
pandas
numpy
scikit-learn
joblib
unittest