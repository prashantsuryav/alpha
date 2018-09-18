import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

StockReturns = pd.read_csv('resources/Big9Returns2017.csv', parse_dates=['Date'])['AAPL']

# Set the simulation parameters
mu = np.mean(StockReturns)
vol = np.std(StockReturns)
T = 252
S0 = 10

# Add one to the random returns
rand_rets = np.random.normal(mu, vol, T) + 1

# Forecasted random walk
forecasted_values = rand_rets.cumprod()*S0

# Plot the random walk
plt.plot(range(0, T), forecasted_values)
plt.show()

# Loop through 100 simulations
for i in range(0, 10):
    # Generate the random returns
    rand_rets = np.random.normal(mu, vol, T) + 1

    # Create the Monte carlo path
    forecasted_values = S0 * (rand_rets).cumprod()

    # Plot the Monte Carlo path
    plt.plot(range(T), forecasted_values)

# Show the simulations
plt.show()

# 3
# Aggregate the returns
sim_returns = []
# Loop through 100 simulations
for i in range(100):
    # Generate the Random Walk
    rand_rets = np.random.normal(mu, vol, T)

    # Save the results
    sim_returns.append(rand_rets)
# Calculate the VaR(99)
var_99 = np.percentile(sim_returns, 1)
print("Parametric VaR(99): ", round(100 * var_99, 2), "%")