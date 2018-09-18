import pandas as pd
import matplotlib.pyplot as plt

df_qqq = pd.read_csv('resources/QQQ.csv', parse_dates=['Date'])
df_amd = pd.read_csv('resources/AMD.csv', parse_dates=['Date'])


def give_me_raw_data():
    return df_qqq


def give_processed_data():
    print(df_qqq.head())
    print(df_amd.head())

    # Plot the Adj_Close columns for SPY and LNG
    df_qqq['Adj_Close'].plot(label='QQQ', legend=True)
    df_amd['Adj_Close'].plot(label='AMD', legend=True, secondary_y=True)
    # plt.show()  # show the plot
    plt.clf()  # clear the plot space

    # Histogram of the daily price change percent of Adj_Close for LNG
    df_qqq['Adj_Close'].pct_change().plot.hist(bins=50)
    plt.xlabel('adjusted close 1-day percent change')
    # plt.show()

    # Create 5-day % changes of Adj_Close for the current day, and 5 days in the future
    df_qqq['5d_future_close'] = df_qqq['Adj_Close'].shift(-5)
    df_qqq['5d_close_future_pct'] = df_qqq['5d_future_close'].pct_change(5)
    df_qqq['5d_close_pct'] = df_qqq['Adj_Close'].pct_change(5)

    # Calculate the correlation matrix between the 5d close pecentage changes (current and future)
    corr = df_qqq[['5d_close_pct', '5d_close_future_pct']].corr()
    print(corr)

    # Scatter the current 5-day percent change vs the future 5-day percent change
    plt.scatter(df_qqq['5d_close_pct'], df_qqq['5d_close_future_pct'])
    # plt.show()

    return df_qqq


