import quandl
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2

aapl = quandl.get("WIKI/AAPL", start_date="2015-01-01", end_date="2018-01-01")

aapl.to_csv('resources/aapl_ohlc.csv')
df = pd.read_csv('resources/aapl_ohlc.csv', header=0, index_col='Date', parse_dates=True)

print(df.head())
print(df.tail())
print(df.describe())

aapl['Close'].plot(grid=True)
df['High'].plot(grid=True)
df['Low'].plot(grid=True)
plt.show()
df['Volume'].plot(grid=True)
plt2.show()