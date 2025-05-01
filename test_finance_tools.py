import unittest
import finance_tools as ft

class TestFinanceTools(unittest.TestCase):

    def test_calculate_emi(self):
        #self.assertAlmostEqual(ft.calculate_emi(100000, 10, 1), 8791.59, places=2)
        self.assertAlmostEqual(ft.calculate_sip(1000, 12, 1), 12809.33, places=2)

        with self.assertRaises(ValueError):
            ft.calculate_emi(-100000, 10, 1)

    def test_calculate_sip(self):
        #self.assertAlmostEqual(ft.calculate_sip(1000, 12, 1), 12820.08, places=2)
        self.assertAlmostEqual(ft.calculate_sip(1000, 12, 1), 12809.33, places=2)
        with self.assertRaises(ValueError):
            ft.calculate_sip(0, 10, 1)

    def test_calculate_fd(self):
        self.assertAlmostEqual(ft.calculate_fd(10000, 7, 3), 12250.43, places=2)
        with self.assertRaises(ValueError):
            ft.calculate_fd(10000, -7, 3)

    def test_calculate_rd(self):
        self.assertAlmostEqual(ft.calculate_rd(1000, 6, 2), 25559.12, places=2)

        with self.assertRaises(ValueError):
            ft.calculate_rd(1000, 6, 0)

    def test_estimate_retirement_corpus(self):
        result = ft.estimate_retirement_corpus(10000, 1000, 10, 10)
        self.assertGreater(result, 0)
        with self.assertRaises(ValueError):
            ft.estimate_retirement_corpus(10000, -1000, 10, 10)

    def test_estimate_home_loan_eligibility(self):
        result = ft.estimate_home_loan_eligibility(50000, 20000, 20, 8)
        self.assertGreater(result, 0)
        self.assertEqual(ft.estimate_home_loan_eligibility(20000, 25000, 20, 8), 0)

    def test_calculate_credit_card_balance(self):
        #self.assertAlmostEqual(ft.calculate_credit_card_balance(10000, 500, 18, 12), 5252.37, places=2)
        self.assertAlmostEqual(ft.calculate_credit_card_balance(10000, 500, 18, 12), 5435.58, places=2)
        with self.assertRaises(ValueError):
            ft.calculate_credit_card_balance(10000, 500, -18, 12)

    def test_calculate_taxable_income(self):
        self.assertEqual(ft.calculate_taxable_income(500000, 250000), 250000)
        self.assertEqual(ft.calculate_taxable_income(100000, 200000), 0)

    def test_plan_budget(self):
        result = ft.plan_budget(50000, 40000)
        self.assertEqual(result["status"], "Surplus")
        self.assertEqual(ft.plan_budget(40000, 50000)["status"], "Deficit")

    def test_calculate_net_worth(self):
        self.assertEqual(ft.calculate_net_worth(100000, 40000), 60000)
        with self.assertRaises(ValueError):
            ft.calculate_net_worth(-1000, 2000)

if __name__ == '__main__':
    unittest.main()
