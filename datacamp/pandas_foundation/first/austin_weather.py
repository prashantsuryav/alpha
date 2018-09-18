import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('resources/weather_data_austin_2010.csv')
# df['Temperature'].plot(color = 'red')
df.plot()

plt.title('Temperature in Austin')
# Specify the x-axis label
plt.xlabel('Hours since midnight August 1, 2010')
# Specify the y-axis label
plt.ylabel('Temperature (degrees F)')

plt.show()

# Plot all columns (default)
df.plot()
plt.show()

# Plot all columns as subplots
df.plot(subplots=True)
plt.show()

# Plot just the Dew Point data
column_list1 = ['DewPoint']
df[column_list1].plot()
plt.show()

# Plot the Dew Point and Temperature data, but not the Pressure data
column_list2 = ['Temperature', 'DewPoint']
df[column_list2].plot()
plt.show()

