import pandas as pd

df = pd.read_csv('resources/austin_airport_departure_data_2015_july.csv', header=10, parse_dates=['Date (MM/DD/YYYY)'], index_col=['Date (MM/DD/YYYY)'])

print(df.columns)
df1 = df.columns.str.strip()
print(df.head())

dallas = df['Destination Airport '].str.contains('DAL')
print(dallas.count())
print(dallas.sum())
daily_departures = dallas.resample('D').sum()
print('daily departures from dallas', daily_departures)
daily_departures.describe()

mask = df['Destination Airport '] == 'LAX'
la = df[mask]
print('FromHere')
print(la.columns.values)
print(la)

# Combine two columns of data to create a datetime series: times_tz_none
times_tz_none = pd.to_datetime(la['Wheels-off Time'])
# Localize the time to US/Central: times_tz_central
times_tz_central = times_tz_none.dt.tz_localize('US/Central')
# Convert the datetimes from US/Central to US/Pacific
times_tz_pacific = times_tz_central.dt.tz_convert('US/Pacific')