import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import yfinance as yf


# Importing data
def get_data(stocks, start, end):
    stockData = yf.download(stocks, start=start, end=end)['Close']
    if isinstance(stockData, pd.Series):
        stockData = stockData.to_frame()

    returns = stockData.pct_change().dropna()
    meanReturns = returns.mean()
    covMatrix = returns.cov()
    return meanReturns, covMatrix


stockList = ['CBA', 'BHP', 'TLS', 'NAB', 'WBC', 'STO']
stocks = [stock + '.AX' for stock in stockList]
endDate = dt.datetime.now()
startDate = endDate - dt.timedelta(days=300)

meanReturns, covMatrix = get_data(stocks, startDate, endDate)

weights = np.random.random(len(meanReturns))
weights /= np.sum(weights)

# Monte Carlo settings
mc_sims = 10000
T = 100
initial_portfolio = 10000

# Convert to numpy arrays
meanReturns = meanReturns.values
covMatrix = covMatrix.values

# Cholesky decomposition
L = np.linalg.cholesky(covMatrix)

# Store all simulated portfolio paths
portfolio_sims = np.zeros((T, mc_sims))

for m in range(mc_sims):
    Z = np.random.normal(size=(T, len(weights)))
    dailyReturns = meanReturns + Z @ L.T
    portfolio_return_path = dailyReturns @ weights
    portfolio_value = np.cumprod(1 + portfolio_return_path) * initial_portfolio
    portfolio_sims[:, m] = portfolio_value

plt.plot(portfolio_sims)
plt.ylabel('Portfolio Value ($)')
plt.xlabel('Days')
plt.title('MC Simulation of a stock portfolio')
plt.show()

def mcVaR(returns, alpha=5):
    """ Input: Pandas series of returns
        Output: Percentile on return distribution to a given confidence level alpha 
    """
    if isinstance(returns, pd.Series):
        return np.percentile(returns, alpha)
    else:
        raise TypeError("Expected a pandas data series.")
    
def mcCVaR(returns, alpha=5):
    """ Input: Pandas series of returns
        Output: CVaR or expected shortfall to a given confidence level alpha
    """
    if isinstance(returns, pd.Series):
        var = mcVaR(returns, alpha=alpha)
        belowVaR = returns <= var
        return returns[belowVaR].mean()
    else:
        raise TypeError("Expected a pandas data series.")
     
final_values = pd.Series(portfolio_sims[-1])

VaR = initial_portfolio - mcVaR(final_values, alpha=5)
CVaR = initial_portfolio - mcCVaR(final_values, alpha=5)

print('VaR ${}' .format(round(VaR, 2)))
print('CVaR ${}' .format(round(VaR, 2)))