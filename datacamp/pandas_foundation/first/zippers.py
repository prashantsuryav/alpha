import pandas as pd

list_keys = ['Country' , 'Total']
list_values = [['US' ,'CHINA', 'INDIA'], [100, 200, 15]]

zipped = list(zip(list_keys, list_values))

print(zipped)

data = dict(zipped)
print(data)

df = pd.DataFrame(data)
print(df)

list_labels = ['New Country', 'New Total']
df.columns = list_labels

print(df)

cities = ['Ujjain', 'Ratlam', 'Nagda', 'Bhopal']
state = 'MP'

data = {'state': state, 'city': cities}
df = pd.DataFrame(data)

print(df)
