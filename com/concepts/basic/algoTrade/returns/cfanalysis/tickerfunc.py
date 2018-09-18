import pandas as pd
import quandl
import datetime
import matplotlib.pyplot as plt


def get(tickers, startdate, enddate):
    def data(ticker):
        return quandl.get("WIKI/" + ticker, start_date=startdate, end_date=enddate)

    datas = map(data, tickers)
    return pd.concat(datas, keys=tickers, names=['Ticker', 'Date'])


tickers = ['AAPL', 'MSFT', 'IBM', 'GOOG']
all_data = get(tickers, datetime.datetime(2014, 1, 1), datetime.datetime(2016, 1, 1))

daily_close_px = all_data[['Adj. Close']].reset_index().pivot('Date', 'Ticker', 'Adj. Close')
daily_pct_change = daily_close_px.pct_change()

# daily_pct_change.hist(bins=50, sharex=True)

pd.plotting.scatter_matrix(daily_pct_change, diagonal='kde', alpha=0.1, figsize=(12,12))

plt.show()