def allocate_case(account_risk, dca_trust):
    if account_risk == "HIGH" and dca_trust == "HIGH":
        return "Assign to Tier-1 DCA"
    return "Assign to Standard DCA"
