import pandas as pd

df = pd.read_csv('resources/auto-mpg.csv')

global_mean = df.mean()
global_std = df.std()
print(global_mean)

us = df[df['origin'] == 'US']
us_mean = us.mean()
us_std = us.std()

print(us_mean)
