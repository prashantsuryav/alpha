import quandl
import matplotlib.pyplot as plt
import numpy as np

aapl = quandl.get("WIKI/AAPL", start_date="2015-01-01", end_date="2018-01-01")

# Isolate the adjusted closing prices
adj_close_px = aapl['Adj. Close']

# Calculate the moving average
moving_avg = adj_close_px.rolling(window=40).mean()

# Inspect the result
print(moving_avg[-10:])

# Short moving window rolling mean
aapl['42'] = adj_close_px.rolling(window=40).mean()

# Long moving window rolling mean
aapl['252'] = adj_close_px.rolling(window=252).mean()

# Plot the adjusted closing price, the short and long windows of rolling means
aapl[['Adj. Close', '42', '252']].plot()

# Define the minumum of periods to consider
min_periods = 75

adj_close_px = aapl['Close']

daily_pct_change = adj_close_px.pct_change()

# Calculate the volatility
vol = daily_pct_change.rolling(min_periods).std() * np.sqrt(min_periods)

# Plot the volatility
vol.plot(figsize=(10, 8))

# Show plot
plt.show()