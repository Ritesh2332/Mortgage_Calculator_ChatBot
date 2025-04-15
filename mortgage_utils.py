def calculate_mortgage_payment(principal, annual_rate, years):
    monthly_rate = annual_rate / 12 / 100
    total_months = years * 12
    if monthly_rate == 0:
        return principal / total_months
    payment = principal * (monthly_rate * (1 + monthly_rate)**total_months) / ((1 + monthly_rate)**total_months - 1)
    return round(payment, 2)
