import math

def calculate_emi(principal, annual_rate, tenure_years):
    """Calculate EMI (monthly installment)."""
    if principal <= 0 or annual_rate <= 0 or tenure_years <= 0:
        raise ValueError("Inputs must be positive")
    r = annual_rate / 12 / 100
    n = tenure_years * 12
    emi = principal * r * (1 + r)**n / ((1 + r)**n - 1)
    return round(emi, 2)

def calculate_sip(monthly_investment, annual_rate, years):
    """Calculate SIP maturity amount."""
    if monthly_investment <= 0 or annual_rate <= 0 or years <= 0:
        raise ValueError("Inputs must be positive")
    n = years * 12
    r = annual_rate / 12 / 100
    amount = monthly_investment * ((1 + r)**n - 1) * (1 + r) / r
    return round(amount, 2)

def calculate_fd(principal, annual_rate, years):
    """Calculate FD maturity amount."""
    if principal <= 0 or annual_rate <= 0 or years <= 0:
        raise ValueError("Inputs must be positive")
    amount = principal * (1 + annual_rate / 100)**years
    return round(amount, 2)

def calculate_rd(monthly_deposit, annual_rate, years):
    """Calculate RD maturity amount with monthly compounding."""
    if monthly_deposit <= 0 or annual_rate <= 0 or years <= 0:
        raise ValueError("Inputs must be positive")
    n = years * 12
    r = annual_rate / 12 / 100
    maturity_value = monthly_deposit * (((1 + r) ** n - 1) / r) * (1 + r)
    return round(maturity_value, 2)

def estimate_retirement_corpus(current_savings, monthly_addition, annual_rate, years):
    """Estimate retirement savings corpus."""
    if any(x < 0 for x in [current_savings, monthly_addition, annual_rate, years]):
        raise ValueError("Inputs must be non-negative")
    r = annual_rate / 12 / 100
    n = years * 12
    future_value = current_savings * (1 + r)**n + monthly_addition * (((1 + r)**n - 1) * (1 + r)) / r
    return round(future_value, 2)

def estimate_home_loan_eligibility(monthly_income, monthly_expenses, loan_tenure_years, interest_rate):
    """Estimate maximum home loan based on income."""
    if monthly_income <= 0 or loan_tenure_years <= 0 or interest_rate <= 0:
        raise ValueError("Inputs must be positive")
    disposable_income = monthly_income - monthly_expenses
    if disposable_income <= 0:
        return 0
    r = interest_rate / 12 / 100
    n = loan_tenure_years * 12
    max_loan = disposable_income * ((1 + r)**n - 1) / (r * (1 + r)**n)
    return round(max_loan, 2)

def calculate_credit_card_balance(balance, monthly_payment, annual_rate, months):
    """Calculate credit card balance if only minimum payment is made."""
    if balance <= 0 or monthly_payment <= 0 or annual_rate <= 0 or months <= 0:
        raise ValueError("Inputs must be positive")
    r = annual_rate / 12 / 100
    for _ in range(months):
        balance = balance * (1 + r) - monthly_payment
        if balance <= 0:
            return 0.0
    return round(balance, 2)

def calculate_taxable_income(gross_income, deductions):
    """Compute taxable income."""
    if gross_income < 0 or deductions < 0:
        raise ValueError("Inputs must be non-negative")
    taxable = gross_income - deductions
    return max(0, round(taxable, 2))

def plan_budget(income, expenses):
    """Suggest savings based on income and expenses."""
    if income < 0 or expenses < 0:
        raise ValueError("Inputs must be non-negative")
    savings = income - expenses
    return {"savings": round(savings, 2), "status": "Surplus" if savings > 0 else "Deficit"}

def calculate_net_worth(assets, liabilities):
    """Calculate net worth."""
    if assets < 0 or liabilities < 0:
        raise ValueError("Inputs must be non-negative")
    return round(assets - liabilities, 2)
