# Monte Carlo Portfolio Risk Analysis (with VaR & CVaR)

## Overview
This project implements a Monte Carlo simulation in Python to model possible future paths of a multi-asset portfolio and estimate downside risk using Value at Risk (VaR) and Conditional Value at Risk (CVaR).
The model downloads historical closing price data for a set of stocks, converts these prices into daily returns, estimates mean returns and the covariance matrix, and then simulates correlated future returns using a multivariate normal framework and Cholesky decomposition.

<img width="948" height="760" alt="image" src="https://github.com/user-attachments/assets/340c43ba-cc96-4418-a935-6373dbe89289" />

## Objectives
- Retrieve and process historical market data
- Estimate average returns and cross-asset covariance
- Simulate correlated portfolio return paths
- Convert simulated returns into portfolio value paths
- Estimate portfolio downside risk using VaR and CVaR

##  Approach

- Retrieved historical price data using yFinance  
- Converted prices to daily returns  
- Estimated mean returns and covariance matrix  
- Generated correlated returns using Cholesky decomposition  
- Simulated 10,000 portfolio paths over 100 days  
- Computed portfolio value via compounding  
- Estimated downside risk using VaR and CVaR

## Technologies Used
- Python
- NumPy
- Pandas
- Matplotlib
- yFinance

## Assumptions and Limitations
This model makes several simplifying assumptions:

- returns are simulated using a multivariate normal structure
- historical mean returns and covariance are treated as stable
- portfolio weights are fixed during the simulation
- transaction costs, rebalancing, and market frictions are ignored
- extreme tail behaviour is not modelled explicitly

## Possible Extensions
- use log returns instead of simple percentage returns
- vectorise the simulation for better performance
- test alternative return distributions with fatter tails
- add portfolio optimisation rather than random weights
- include stress testing and scenario analysis
