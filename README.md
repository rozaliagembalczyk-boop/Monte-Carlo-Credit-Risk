# Monte Carlo Credit Risk & VaR Simulator (Python)

## Overview
This project is a **Monte Carlo simulation engine** designed to estimate portfolio-level credit risk.
It simulates thousands of possible economic scenarios to model **loan defaults** and calculate risk metrics such as:

- Value at Risk (VaR)
- Expected Shortfall (ES)
- Worst-case portfolio loss

The simulator is built using **Python, NumPy, Pandas**, and produces both numerical and visual outputs.

---

## Dataset
The input dataset contains loan-level features such as:

- loan amount (principal / EAD proxy)
- interest rate
- credit grade (A–G)
- loan status

The dataset is stored in: data/loan_data.csv


---

## Methodology

### 1. PD Assignment
Each loan is assigned a **Probability of Default (PD)** based on its credit grade:

| Grade | PD |
|------|----|
| A | 1% |
| B | 2% |
| C | 4% |
| D | 7% |
| E | 12% |
| F | 20% |
| G | 30% |

### 2. LGD and EAD
Loss Given Default (LGD) is assumed to be random between 40% and 60%:

LGD ~ Uniform(0.4, 0.6)

Exposure at Default (EAD) is approximated as:

EAD = loan_amount

Loss if default occurs:

Loss = EAD × LGD

### 3. Monte Carlo Simulation
For each scenario, the simulator generates random numbers for each loan:

- if rand < PD → default occurs
- portfolio loss = sum(losses across defaulted loans)

The simulation produces a distribution of total portfolio losses.

---

## Risk Metrics

### Value at Risk (VaR)
VaR at confidence level α is the percentile loss threshold:

VaR95 = 95th percentile of losses  
VaR99 = 99th percentile of losses

### Expected Shortfall (ES)
Expected Shortfall is the mean loss beyond the VaR threshold:

ES95 = mean(losses ≥ VaR95)

---

## Stress Testing
A stress scenario is included where PD values are increased by a multiplier:

PD_stress = min(PD × 1.5, 1.0)

This represents recession-like credit deterioration.

---

## Outputs
After execution, the simulator produces:

- `outputs/risk_summary.csv` → table of risk metrics
- `outputs/loss_distribution.png` → histogram of simulated loss distribution

---
## Technologies Used
- Python
- NumPy
- Pandas
- Matplotlib

## Example Use Case

This project reflects how banks estimate portfolio credit risk using scenario-based simulation, and demonstrates
quantitative risk analytics skills relevant to:

- Credit Risk

- Market Risk (VaR modelling)

- Risk Reporting

- Financial Analytics
---
## How to Run

### Install dependencies
```bash
pip install -r requirements.txt




