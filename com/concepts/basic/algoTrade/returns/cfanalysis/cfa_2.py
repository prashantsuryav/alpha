import quandl
import matplotlib.pyplot as plt

aapl = quandl.get("WIKI/AAPL", start_date="2015-01-01", end_date="2018-01-01")

monthly = aapl.resample('BM').apply(lambda x: x[-1])

monthly.pct_change()

quarter = aapl.resample("4M").mean()

quarter.pct_change()

daily_close = aapl[['Close']]

daily_pct_change = daily_close / daily_close.shift(1) - 1
daily_pct_change.hist(bins=50)

cum_daily_return = (1 + daily_pct_change).cumprod()
cum_daily_return.plot(grid=True)
# print(daily_pct_change)

# daily_pct_change.plot(grid=True)
plt.show()