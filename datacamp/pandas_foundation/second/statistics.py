import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('resources/percent-bachelors-degrees-women-usa.csv', index_col=['Year'])
print(df)

print(df['Engineering'].min())
print(df['Engineering'].max())

# df['Engineering'].plot()

mean = df.mean(axis = 'columns')
mean.plot()

plt.show()