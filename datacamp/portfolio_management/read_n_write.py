import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import skew
from scipy.stats import kurtosis
from scipy.stats import shapiro

# Microsoft_Stock_Data
stock_data = pd.read_csv('resources/MSFTPrices.csv', parse_dates=['Date'])
sorted_stock_data = stock_data.sort_values(by=['Date'])
print(sorted_stock_data.head())

sorted_stock_data['Returns'] = sorted_stock_data['Adjusted'].pct_change()
print(sorted_stock_data['Returns'].head())
print(sorted_stock_data.head())

stock_returns = sorted_stock_data['Returns']
stock_returns.plot()
plt.show()

percentage_change = stock_returns*100
plt.hist(percentage_change.dropna(), bins=75, density=False)
plt.show()


mean_daily_return = np.mean(stock_returns)
print(stock_returns)
print(mean_daily_return)

# Calculate annual
annualised_return = (1 + mean_daily_return) ** 252 - 1
print(annualised_return)

sigma_daily = np.std(stock_returns)
print('sigma ', sigma_daily)

variance_daily = np.square(sigma_daily)
print('variance ', variance_daily)

# annualised
annualised_sigma = sigma_daily*np.sqrt(252)
print('annualised_sigma ', annualised_sigma)

annualised_variance = np.square(annualised_sigma)
print('annualised_variance ', annualised_variance)

clear_returns = stock_returns.dropna()
skew = skew(clear_returns)
print('kurtosis ', skew)

excess_kurtosis = kurtosis(clear_returns)
print('excess_kurtosis', excess_kurtosis)
print('actual_kurtosis', excess_kurtosis + 3)

# Shapiro-wiki test
saphiro_results = shapiro(clear_returns)
print('p-value' , saphiro_results[1] , ' ,', saphiro_results[0])