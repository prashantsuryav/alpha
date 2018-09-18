import pandas as pd

df1 = pd.read_csv('resources/readMe.txt')
print(df1.head())
df2 = pd.read_csv('resources/readMe.txt', delimiter=' ', header=3, comment='#')
print(df2.head())
df2.to_csv('resources/file_clean', index= False)
df2.to_excel('resources/file_clean.xlsx', index= False)