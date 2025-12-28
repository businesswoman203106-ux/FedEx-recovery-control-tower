def calculate_risk(days_due, amount):
    if days_due > 60 or amount > 50000:
        return "HIGH"
    return "LOW"

def calculate_trust(success_rate):
    if success_rate > 80:
        return "HIGH"
    return "LOW"
