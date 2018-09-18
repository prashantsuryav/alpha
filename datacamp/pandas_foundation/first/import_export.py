import pandas as pd

df1 = pd.read_csv('resources/world_population.csv')
print(df1)
new_lables = ['Years', 'population']

df2 = pd.read_csv('resources/world_population.csv', header=0, names=new_lables)
print(df2)