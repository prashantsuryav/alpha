import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('resources/ts1.csv', delimiter="     ", header=None)
df.columns = ['Date', 'Frequency']
print(df)
my_datetimes = pd.to_datetime(df['Date'].tolist())
ts1 = pd.Series(df['Frequency'].tolist(), index=my_datetimes)
ts1.plot()
print(ts1)

df2 = pd.read_csv('resources/ts2.csv', delimiter="     ", header=None)
df2.columns = ['Date', 'Frequency']
my_datetimes_2 = pd.to_datetime(df2['Date'].tolist())
ts2 = pd.Series(df2['Frequency'].tolist(), index=my_datetimes_2)
ts2.plot()
plt.show()
print(ts2)

ts2_inter = ts2.reindex(ts1.index).interpolate(how='linear')
ts2_inter.plot()
plt.show()
print(ts2_inter)

differences = np.abs(ts1 - ts2_inter)
print('stats: ', differences.describe())