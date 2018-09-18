import quandl
import pandas as pd

aapl = quandl.get("WIKI/AAPL", start_date="2015-01-01", end_date="2018-01-01")

print(aapl.index)
print(aapl.columns)
print(aapl['Close'][-10:])
print(aapl.loc[pd.Timestamp('2006-11-01'):pd.Timestamp('2006-12-31')])
print(aapl.loc['2007'])
print(aapl.iloc[22:43])
print(aapl.iloc[[22,43], [0,3]])

print(aapl.sample(20))
print(aapl.resample('M').mean())
print(aapl.asfreq("M", method="bfill"))