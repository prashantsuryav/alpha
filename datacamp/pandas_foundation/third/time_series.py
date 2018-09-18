import pandas as pd

# Prepare a format string: time_format
time_format='%Y-%m-%d %H%M%S'

# Convert date_list into a datetime object: my_datetimes
my_datetimes = pd.to_datetime(['2015-01-01 091234','2015-01-02 091234', '2015-02-01 091234', '2015-03-01 091234'],
                              format=time_format)

temperature_list = [120, 310, 550, 690]
# Construct a pandas Series using temperature_list and my_datetimes: time_series
time_series = pd.Series(temperature_list, index=my_datetimes)

print(time_series.loc['2015-01-01':'2015-01-30'])
print(time_series.loc['2014-01-01':'2017-01-30'])

simple_index = [1,2,3,4]
new_series = time_series.reindex(simple_index)
# new_series_2 = time_series.reindex(simple_index, method = "ffill")
print(new_series)