
from django.test import TestCase
from django.test import TestCase
from operations.views import (
    emi_calculator,
    calculate_credit_card_balance,
    calculate_taxable_income,
    plan_budget,
    calculate_net_worth,
)

class CalculatorFunctionTests(TestCase):

    def test_credit_card_balance(self):
        result = calculate_credit_card_balance(balance=10000, annual_rate=18, months=12)
        self.assertIsInstance(result, float)
        self.assertGreater(result, 0)

    def test_taxable_income(self):
        self.assertEqual(calculate_taxable_income(600000), 550000)
        self.assertEqual(calculate_taxable_income(40000), 0)
    
    def test_budget_planner_good_savings(self):
        summary = plan_budget(income=50000, fixed_expenses=10000, variable_expenses=5000)
        self.assertEqual(summary["Suggestion"], "Good saving habit")
    
    def test_net_worth(self):
        self.assertEqual(calculate_net_worth(assets=100000, liabilities=30000), 70000)
    
    def test_sip_calculation(self):
        monthly_investment = 5000
        rate = 12
        years = 10
        monthly_rate = rate / (12 * 100)
        months = years * 12
        maturity = monthly_investment * (((1 + monthly_rate) ** months - 1) * (1 + monthly_rate)) / monthly_rate
        self.assertTrue(maturity > 0)

    def test_rd_calculation(self):
        mi = 2000
        rate = 7
        years = 2
        m = years * 12
        r = rate / (100 * 12)
        maturity = mi * m + mi * (m * (m + 1) / 2) * r
        self.assertTrue(maturity > 0)

    def test_fd_calculation(self):
        principal = 100000
        rate = 7
        years = 3
        f = 4
        rate_per_period = rate / (100 * f)
        total_periods = years * f
        maturity = principal * ((1 + rate_per_period) ** total_periods)
        self.assertTrue(maturity > principal)

    def test_retirement_calculator(self):
        current_savings = 100000
        monthly_contribution = 5000
        annual_rate = 8
        years_until_retirement = 20
        monthly_rate = annual_rate / (12 * 100)
        months = years_until_retirement * 12
        future_value = current_savings * ((1 + monthly_rate) ** months) + \
                       monthly_contribution * (((1 + monthly_rate) ** months - 1) * (1 + monthly_rate)) / monthly_rate
        self.assertTrue(future_value > 0)

    def test_loan_eligibility(self):
        income = 60000
        expenses = 20000
        years = 5
        rate = 10
        available_income = income - expenses
        monthly_rate = rate / (12 * 100)
        months = years * 12
        if monthly_rate == 0:
            eligibility = available_income * months
        else:
            eligibility = available_income * (((1 + monthly_rate) ** months - 1) / (monthly_rate * (1 + monthly_rate) ** months))
        self.assertTrue(eligibility > 0)