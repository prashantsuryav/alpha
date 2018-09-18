import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('resources/life_expectancy_at_birth.csv')
print(df['2015'].count())

print(df.quantile([0.05, 0.95]))

years = ['1800', '1850', '1900', '1950', '2000']
df[years].plot(kind='box')
plt.show()