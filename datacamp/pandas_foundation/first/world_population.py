import numpy as np
import pandas as pd

df = pd.read_csv('resources/world_population.csv')
print(df['Year'].head())

np_vals = df.values

np_vals_log10 = np.log10(np_vals)

df_log10 = np.log10(df)

[print(x, 'has type', type(eval(x))) for x in ['np_vals', 'np_vals_log10', 'df', 'df_log10']]