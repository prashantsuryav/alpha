import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

cum_rets = pd.read_csv('resources/USO_2.csv')
cum_rets = cum_rets.drop(columns=['Date'])

# Drawdown
# Calculate the running maximum
running_max = np.maximum.accumulate(cum_rets)
# Ensure the value never drops below 1
running_max[running_max < 1] = 1
# Calculate the percentage drawdown
drawdown = (cum_rets)/running_max - 1
# Plot the results
drawdown.plot()
plt.show()


# stock_data = pd.read_csv('resources/Big9Returns2017.csv', parse_dates=['Date'])
# returns_data = stock_data.drop(columns= ['Date'])
# StockReturns_perc = cum_rets.pct_change()
StockReturns_perc = cum_rets

# Historical value at risk
# Calculate historical VaR(95)
var_95 = np.percentile(StockReturns_perc, 5)
print(var_95)
# Sort the returns for plotting
sorted_rets = StockReturns_perc.sort_values(by= ['USO'])
# Plot the probability of each sorted return quantile
plt.hist(sorted_rets, density=True)
# Denote the VaR 95 quantile
plt.axvline(x=var_95, color='r', linestyle='-', label="VaR 95: {0:.2f}%".format(var_95))
plt.show()


# Historical CVaR 95
cvar_95 = StockReturns_perc[StockReturns_perc <= var_95].mean()
print(cvar_95)
# Sort the returns for plotting
sorted_rets = sorted(StockReturns_perc)
# Plot the probability of each return quantile
plt.hist(sorted_rets, density=True)
# Denote the VaR 95 and CVaR 95 quantiles
plt.axvline(x=var_95, color="r", linestyle="-", label='VaR 95: {0:.2f}%'.format(var_95))
plt.axvline(x=cvar_95, color='b', linestyle='--', label=cvar_95)
plt.show()