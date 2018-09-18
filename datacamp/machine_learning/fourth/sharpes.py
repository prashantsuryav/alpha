# We need to find the "ideal" portfolios for each date so we can use them as targets for machine learning.
# We'll loop through each date in portfolio_returns, then loop through the portfolios we generated with
# portfolio_returns[date]. We'll then calculate the Sharpe ratio, which is the return divided by volatility
# (assuming a no-risk return of 0).
# We use enumerate() to loop through the returns for the current date (portfolio_returns[date]) and keep
# track of the index with i. Then we use the current date and current index to get the volatility of each portfolio with
# portfolio_volatility[date][i]. Finally, we get the index of the best Sharpe ratio for each date using np.argmax().
# We'll use this index to get the ideal portfolio weights soon.

from datacamp.machine_learning.fourth import mpt
import numpy as np
import matplotlib.pyplot as plt

# Empty dictionaries for sharpe ratios and best sharpe indexes by date
sharpe_ratio, max_sharpe_idxs = {}, {}

portfolio_returns = mpt.portfolio_returns
portfolio_volatility = mpt.portfolio_volatility
# Loop through dates and get sharpe ratio for each portfolio
for date in portfolio_returns.keys():
    for i, ret in enumerate(portfolio_returns[date]):
        # Divide returns by the volatility for the date and index, i
        sharpe_ratio.setdefault(date, []).append(ret / portfolio_volatility[date][i])

    # Get the index of the best sharpe ratio for each date
    max_sharpe_idxs[date] = np.argmax(sharpe_ratio[date])

print(portfolio_returns[date][max_sharpe_idxs[date]])


# Calculate EWMAs
# We will now work towards creating some features to be able to predict our ideal portfolios.
# We will simply use the price movement as a feature for now. To do this we will create a daily
# exponentially-weighted moving average (EWMA), then resample that to the monthly timeframe.
# Finally, we'll shift the monthly moving average of price one month in the future,
# so we can use it as a feature for predicting future portfolios.
# Calculate exponentially-weighted moving average of daily returns
returns_daily = mpt.returns_daily
ewma_daily = returns_daily.ewm(span=30).mean()

# Resample daily returns to first business day of the month with average for that month
ewma_monthly = ewma_daily.resample('BMS').first()

# Shift ewma for the month by 1 month forward so we can use it as a feature for future predictions
ewma_monthly = ewma_monthly.shift(1).dropna()

print(ewma_monthly.iloc[-1])

# Make features and targets
# To use machine learning to pick the best portfolio, we need to generate features and targets.
# Our features were just created in the last exercise – the exponentially weighted moving averages of prices.
# Our targets will be the best portfolios we found from the highest Sharpe ratio.
#
# We will use pandas' .iterrows() method to get the index, value pairs for the ewma_monthly DataFrame.
# We'll set the current value of ewma_monthly in the loop to be our features.
# Then we'll use the index of the best Sharpe ratio (from max_sharpe_idxs) to get the best portfolio_weights for
# each month and set that as a target.
targets, features = [], []

# Create features from price history and targets as ideal portfolio
portfolio_weights = mpt.portfolio_weights
for date, ewma in ewma_monthly.iterrows():

    # Get the index of the best sharpe ratio
    best_idx = max_sharpe_idxs[date]
    targets.append(portfolio_weights[date][best_idx])
    features.append(ewma)  # add ewma to features

targets = np.array(targets)
features = np.array(features)
print(targets[-5:])

# Plot efficient frontier with best Sharpe ratio
# Let's now plot the efficient frontier again, but add a marker for the portfolio with the best Sharpe index.
# Visualizing our data is always a good idea to better understand it.
# Get most recent (current) returns and volatility
covariances = mpt.covariances
# Get most recent (current) returns and volatility
date = sorted(covariances.keys())[-1]
cur_returns = portfolio_returns[date]
cur_volatility = portfolio_volatility[date]

# Plot efficient frontier with sharpe as point
plt.scatter(x=cur_volatility, y=cur_returns, alpha=0.1, color='blue')
best_idx = max_sharpe_idxs[date]

# Place an orange "X" on the point with the best Sharpe ratio
plt.scatter(x=cur_volatility[best_idx], y=cur_returns[best_idx], marker='x', color='orange')
plt.xlabel('Volatility')
plt.ylabel('Returns')
plt.show()