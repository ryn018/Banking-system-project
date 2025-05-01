import unittest
from predictor_api import predict_loan_amount
import loan_predictor

class TestLoanPredictor(unittest.TestCase):
    def test_prediction_shape(self):
        sample_input = [35, 50000, 700, 5, 100000, 2]
        result = predict_loan_amount(sample_input)
        self.assertIsInstance(result, float)
        self.assertGreater(result, 0)

    def test_pipeline(self):
        loan_predictor.run_pipeline("loan_amount_prediction_dataset_v2.csv")
        self.assertTrue(True)  # Assuming no exception = success

if __name__ == '__main__':
    unittest.main()
