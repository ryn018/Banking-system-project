import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
from math import sqrt

MODEL_PATH = "loan_model.pkl"
SCALER_PATH = "scaler.pkl"

FEATURES = ['Age', 'Monthly_Income', 'Credit_Score', 'Loan_Tenure_Years', 'Existing_Loan_Amount', 'Num_of_Dependents']

def load_data(path):
    df = pd.read_csv(path)
    df.dropna(inplace=True)
    return df

def preprocess(df):
    X = df[FEATURES]
    y = df['Loan_Amount']
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled, y, scaler

def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    #rmse = mean_squared_error(y_test, predictions, squared=False)
    rmse = sqrt(mean_squared_error(y_test, predictions))
    print(f"Model RMSE: {rmse:.2f}")
    return model

def save_model(model, scaler):
    joblib.dump(model, MODEL_PATH)
    joblib.dump(scaler, SCALER_PATH)

def run_pipeline(csv_path):
    df = load_data(csv_path)
    X, y, scaler = preprocess(df)
    model = train_model(X, y)
    save_model(model, scaler)
