from predictor_api import predict_loan_amount

sample = [30, 600000, 740, 50, 100000, 2]
amount = predict_loan_amount(sample)
print(f"Predicted Loan Amount: ₹{amount:,.2f}")
