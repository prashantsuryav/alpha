import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datacamp.portfolio_management.portfolio_investing import get_cumulative_returns

numstocks = 9
RandomPortfolios = pd.read_csv('resources/EfficientFrontierPortfoliosSlim.csv')
StockReturns = pd.read_csv('resources/Big9Returns2017.csv', parse_dates=['Date']).drop(columns= ['Date'])

# Risk free rate
risk_free = 0
# Calculate the Sharpe Ratio for each asset
RandomPortfolios['Sharpe'] = (RandomPortfolios['Returns']-risk_free)/RandomPortfolios['Volatility']
# Print the range of Sharpe ratios
print(RandomPortfolios['Sharpe'].describe()[['min', 'max']])


# BY RETURN
# Sort the portfolios by Sharpe ratio
sorted_portfolios = RandomPortfolios.sort_values(by=['Sharpe'], ascending=False)
# Extract the corresponding weights
MSR_weights = sorted_portfolios.iloc[0, 0:numstocks]
# Cast the MSR weights as a numpy array
MSR_weights_array = np.array(MSR_weights)
# Calculate the MSR portfolio returns
StockReturns['Portfolio_MSR'] = StockReturns.iloc[:, 0:numstocks].mul(MSR_weights_array, axis=1).sum(axis=1)
# Plot the cumulative returns
get_cumulative_returns(StockReturns['Portfolio_MSR'])
# plt.show()


# BY VOLATALITY
# Sort the portfolios by volatility
sorted_portfolios = RandomPortfolios.sort_values(by=['Volatility'], ascending=True)
# Extract the corresponding weights
GMV_weights = sorted_portfolios.iloc[0, 0:numstocks]
# Cast the GMV weights as a numpy array
GMV_weights_array = np.array(GMV_weights)
# Calculate the GMV portfolio returns
StockReturns['Portfolio_GMV'] = StockReturns.iloc[:, 0:numstocks].mul(GMV_weights_array, axis=1).sum(axis=1)
# Plot the cumulative returns
get_cumulative_returns(StockReturns['Portfolio_GMV'])
plt.show()