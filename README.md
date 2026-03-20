# Monte Carlo Portfolio Risk Analysis (with VaR & CVaR)

## Overview
This project implements a Monte Carlo simulation in Python to model possible future paths of a multi-asset portfolio and estimate downside risk using Value at Risk (VaR) and Conditional Value at Risk (CVaR).
The model downloads historical closing price data for a set of stocks, converts these prices into daily returns, estimates mean returns and the covariance matrix, and then simulates correlated future returns using a multivariate normal framework and Cholesky decomposition.

## Objectives
- Retrieve and process historical market data
- Estimate average returns and cross-asset covariance
- Simulate correlated portfolio return paths
- Convert simulated returns into portfolio value paths
- Estimate portfolio downside risk using VaR and CVaR

## Methodology

### 1. Historical data
The project downloads historical closing prices for a selected basket of stocks using `yfinance`.

These prices are converted into daily percentage returns using:

\[
R_t = \frac{P_t - P_{t-1}}{P_{t-1}}
\]

### 2. Estimating model inputs
From the historical return series, the code calculates:
- the mean daily return for each asset
- the covariance matrix of asset returns

These statistics are then used as inputs into the simulation.

### 3. Generating correlated returns
To simulate dependent asset returns, the covariance matrix is factorised using Cholesky decomposition:

\[
\Sigma = LL^T
\]

A matrix of standard normal random variables is generated and transformed to produce correlated return shocks. These shocks are added to the mean return vector to obtain simulated daily returns for each asset.

### 4. Portfolio construction
The code generates a random portfolio weight vector and normalises it so that the weights sum to 1.

Portfolio returns are then computed as the weighted sum of simulated asset returns.

### 5. Portfolio value simulation
For each simulation, daily portfolio returns are compounded from an initial portfolio value to generate a full portfolio path over time.

The model runs many simulations, producing a distribution of possible future portfolio values.

### 6. Risk measures
The final simulated portfolio values are used to estimate:

- **Value at Risk (VaR):** the percentile cutoff of the simulated portfolio value distribution at a chosen confidence level
- **Conditional Value at Risk (CVaR):** the average of outcomes worse than the VaR threshold

These give an estimate of likely downside loss and average tail loss.

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

## Conclusion
This project demonstrates how Monte Carlo simulation can be used to model portfolio uncertainty and estimate downside risk measures such as VaR and CVaR. It provides a practical introduction to stochastic portfolio modelling, correlated asset simulation, and basic quantitative risk analysis.

## Author
Muhammad Khan
