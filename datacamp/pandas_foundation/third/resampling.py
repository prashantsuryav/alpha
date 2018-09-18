import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('resources/weather_data_austin_2010.csv', parse_dates=['Date'], index_col='Date')
temperature = df['Temperature']
temperature.plot()
plt.show()

df1 = temperature.resample('4W').mean()
df1.plot()
plt.show()

df2 = df['Temperature'].resample('200D').mean()
df2.plot()
plt.show()

august = df['Temperature']['2010-August']
august_highs = august.resample('D').max()
print(august_highs)

february = df['Temperature']['2010-February']
february_lows = february.resample('D').min()
print(february_lows)

# Extract data from 2010-Aug-01 to 2010-Aug-15: unsmoothed
unsmoothed = df['Temperature']['2010-Aug-01':'2010-Aug-15']
# Apply a rolling mean with a 24 hour window: smoothed
smoothed = unsmoothed.rolling(window=24).mean()
# Create a new DataFrame with columns smoothed and unsmoothed: august
august = pd.DataFrame({'smoothed':smoothed, 'unsmoothed':unsmoothed})
# Plot both smoothed and unsmoothed data using august.plot().
august.plot()

# Extract the August 2010 data: august
august = df['Temperature']['2010-August']
# Resample to daily data, aggregating by max: daily_highs
daily_highs = august.resample('D').max()
# Use a rolling 7-day window with method chaining to smooth the daily high temperatures in August
daily_highs_smoothed = daily_highs.rolling(window=7).mean()
daily_highs_smoothed.plot()
print(daily_highs_smoothed)
plt.show()



