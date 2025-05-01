import joblib
import numpy as np
import pandas as pd

MODEL_PATH = "loan_model.pkl"
SCALER_PATH = "scaler.pkl"

def predict_loan_amount(user_input):
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    # input_array = np.array(user_input).reshape(1, -1)
    # input_scaled = scaler.transform(input_array)
    FEATURES = ['Age', 'Monthly_Income', 'Credit_Score', 'Loan_Tenure_Years', 'Existing_Loan_Amount', 'Num_of_Dependents']

    input_df = pd.DataFrame([user_input], columns=FEATURES)
    input_scaled = scaler.transform(input_df)
    predicted_amount = model.predict(input_scaled)[0]
    return predicted_amount
