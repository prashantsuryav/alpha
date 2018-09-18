import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def get_cumulative_returns(raw_return):
    cumulative_returns = ((1 + raw_return).cumprod() - 1)
    cumulative_returns.plot()


stock_data = pd.read_csv('resources/Big9Returns2017.csv', parse_dates=['Date'])
returns_data = stock_data.drop(columns= ['Date'])
# sorted_stock_data = stock_data.sort_values(by=['Date'])

# Finish defining the portfolio weights as a numpy array
portfolio_weights = np.array([0.12, 0.15, 0.08, 0.05, 0.09, 0.10, 0.11, 0.14, .16])

# Calculate the weighted stock returns
WeightedReturns = returns_data.mul(portfolio_weights, axis=1)
print(WeightedReturns)

# Calculate the portfolio returns
returns_data['Portfolio'] = WeightedReturns.sum(axis=1)

print(returns_data)

# Plot the cumulative portfolio returns over time
get_cumulative_returns(returns_data["Portfolio"])

# 2 EQUAL_WEIGHTED_PORTFOLIO
# How many stocks are in your portfolio?
num_of_stocks = 9

# Create an array of equal weights across all assets
portfolio_weights_ew = np.repeat(1 / num_of_stocks, num_of_stocks)

# Calculate the equally-weighted portfolio returns
returns_data['Portfolio_EW'] = returns_data.iloc[:, 0:num_of_stocks].mul(portfolio_weights_ew, axis=1).sum(axis=1)
get_cumulative_returns(returns_data['Portfolio_EW'])

# 3 Market-Cap Portfolios
# Create an array of market capitalizations (in billions)
market_capitalizations = np.array([601.51, 469.25, 349.5, 310.48, 299.77, 356.94, 268.88, 331.57, 246.09])

# Calculate the market cap weights
mcap_weights = market_capitalizations/sum(market_capitalizations)

# Calculate the market cap weighted portfolio returns
returns_data['Portfolio_MCap'] = returns_data.iloc[:, 0:9].mul(mcap_weights, axis=1).sum(axis=1)
get_cumulative_returns(returns_data['Portfolio_MCap'])

plt.show()

# Calculate the correlation matrix
correlation_matrix = stock_data.corr()
# Print the correlation matrix
print(correlation_matrix)
sns.heatmap(correlation_matrix)

# Calculate the covariance matrix
cov_mat = stock_data.cov()
# Annualize the co-variance matrix
cov_mat_annual = cov_mat*252
# Print the annualized co-variance matrix
print('Annual Covariance Matrix:  ', cov_mat_annual)


# Calculate the portfolio standard deviation
# transpose
portfolio_volatility = np.sqrt(np.dot(portfolio_weights.T, np.dot(cov_mat_annual, portfolio_weights)))
print(portfolio_volatility)
plt.show()