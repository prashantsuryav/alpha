import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('resources/file_clean')
print(df)

x_columns = ['APPLE', 'IBM']

df.plot(x=x_columns, y='Jan')
plt.show()

# plot(kind='scatter')
# plot(kind='box')