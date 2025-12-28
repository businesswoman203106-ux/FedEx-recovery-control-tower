# FedEx Recovery Control Tower – AI-Driven DCA Trust & Allocation Platform

[![FedEx SMART Hackathon](https://img.shields.io/badge/FedEx%20SMART%20Hackathon-Shaastra%202026-blue)](https://unstop.com/hackathons/fedex-smart-hackathon-shaastra-2026-iit-madras-1610993?rstatus=1)

## Overview
This backend-only project is developed for the **FedEx SMART Hackathon – Shaastra 2026** under the  
**Recovery Control Tower** theme.

The system focuses on **overdue account recovery** by using:
- Risk scoring for accounts  
- Trust scoring for DCAs (Delivery Collection Agents)  
- Smart, rule-based allocation to the appropriate DCA tier  

The objective is to enable **proactive recovery decisions** and **real-time operational visibility**.

---

## End-to-End Pipeline

**Pipeline Explanation:**  
This flow represents the complete lifecycle of overdue account handling in the FedEx Recovery Control Tower.  
AI-assisted risk evaluation and DCA trust assessment work together to ensure **efficient, reliable, and timely allocation decisions**.

---

## Backend Logic Implementation

### 1. Risk Scoring
```python
def calculate_risk(days_due, amount):
    if days_due > 60 or amount > 50000:
        return "HIGH"
    return "LOW"

### 2. Trust Scoring
```python
def calculate_trust(success_rate):
    if success_rate > 80:
        return "HIGH"
    return "LOW"

### 3.Smart Allocation
```python
def allocate_case(account_risk, dca_trust):
    if account_risk == "HIGH" and dca_trust == "HIGH":
        return "Assign to Tier-1 DCA"
    return "Assign to Standard DCA"
