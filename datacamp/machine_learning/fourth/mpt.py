import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

lng_df = pd.read_csv('resources/LNG.csv', delimiter="  ", parse_dates=['Date'], index_col=['Date'])
spy_df = pd.read_csv('resources/SPY.csv', delimiter=" ", parse_dates=['Date'], index_col=['Date'])
smlv_df = pd.read_csv('resources/SMLV.csv', delimiter=" ", parse_dates=['Date'], index_col=['Date'])

# Join 3 stock dataframes together
full_df = pd.concat([lng_df, spy_df, smlv_df], axis=1).dropna()
full_df.dropna()

# Resample the full dataframe to monthly timeframe
monthly_df = full_df.resample('BMS').first()

# Calculate daily returns of stocks
returns_daily = full_df.pct_change()

# Calculate monthly returns of the stocks
returns_monthly = monthly_df.pct_change()
print(returns_monthly.tail())

# Daily covariance of stocks (for each monthly period)
covariances = {}
for i in returns_monthly.index:
    rtd_idx = returns_daily.index

    # Mask daily returns for each month and year, and calculate covariance
    mask = (rtd_idx.month == i.month) & (rtd_idx.year == i.year)

    # Use the mask to get daily returns for the current month and year of monthy returns index
    covariances[i] = returns_daily[mask].cov()
    print(covariances[i])


portfolio_returns, portfolio_volatility, portfolio_weights = {}, {}, {}

# Get portfolio performances at each month
for date in sorted(covariances.keys()):
    cov = covariances[date]
    for portfolio in range(10):
        weights = np.random.random(3)
        weights /= np.sum(weights)
        returns = np.dot(weights, returns_monthly.loc[date])
        volatility = np.sqrt(np.dot(weights.T, np.dot(cov, weights)))
        portfolio_returns.setdefault(date, []).append(returns)
        portfolio_volatility.setdefault(date, []).append(volatility)
        portfolio_weights.setdefault(date, []).append(weights)


# Get latest date of available data
date = sorted(covariances.keys())[-1]

# Plot efficient frontier
# warning: this can take at least 10s for the plot to execute...
plt.scatter(x=portfolio_volatility[date], y=portfolio_returns[date], alpha=0.1)
plt.xlabel('Volatility')
plt.ylabel('Returns')
plt.show()