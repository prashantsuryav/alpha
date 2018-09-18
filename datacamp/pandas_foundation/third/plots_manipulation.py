import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv('resources/weather_data_austin_2010.csv', parse_dates=['Date'], index_col=['Date'])
df = pd.read_csv('resources/weather_data_austin_2010.csv')
df['Temperature'].plot()
plt.show()

print(df.columns.values)
df.Date = pd.to_datetime(df['Date'])

df.set_index('Date', inplace=True)
df.plot()
plt.show()

df.Temperature['2010-Jun':'2010-Aug'].plot()
plt.show()
plt.clf()

df.Temperature['2010-06-10':'2010-06-17'].plot()
plt.show()
plt.clf()