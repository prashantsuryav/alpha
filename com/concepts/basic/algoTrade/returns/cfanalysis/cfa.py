import numpy as np
import quandl
import matplotlib.pyplot as plt

aapl = quandl.get("WIKI/AAPL", start_date="2015-01-01", end_date="2018-01-01")

# print(aapl.describe())
daily_close = aapl[['Close']]

daily_pct_change = daily_close.pct_change()

daily_pct_change.fillna(0, inplace=True)

print(daily_pct_change)

daily_log_returns = np.log(daily_close.pct_change()+1)

print(daily_log_returns)

daily_pct_change.plot(grid=True)
daily_log_returns.plot(grid=True)
plt.show()