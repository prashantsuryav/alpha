# Make predictions with a random forest
# In order to fit a machine learning model to predict ideal portfolios, we need to create train and test sets
# for evaluating performance. We will do this as we did in previous chapters, where we take our features and
# targets arrays, and split them based on a train_size we set. Often the train size may be around 70-90% of our data.
#
# We then fit our model (a random forest in this case) to the training data, and evaluate the R2 scores on train
#  and test using .score() from our model. In this case, the hyperparameters have been set for you, but usually
# you'd want to do a search with ParameterGrid like we did in previous chapters

# Make train and test features
from datacamp.machine_learning.first import indicators
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

features, targets = indicators.give_me_features_and_targets()

train_size = int(0.85 * features.shape[0])

train_features = features[:train_size]
test_features = features[train_size:]
train_targets = targets[:train_size]
test_targets = targets[train_size:]

# Fit the model and check scores on train and test
rfr = RandomForestRegressor(n_estimators=300, random_state=42)
rfr.fit(train_features, train_targets)
print(rfr.score(train_features, train_targets))
print(rfr.score(test_features, test_targets))


# Get predictions from model on train and test
train_predictions = rfr.predict(train_features)
test_predictions = rfr.predict(test_features)

df = pd.read_csv('resources/QQQ.csv', parse_dates=['Date'], index_col=['Date'])
df.dropna()
monthly_df = df.resample('BMS').first()
returns_monthly = monthly_df.pct_change()

# Calculate and plot returns from our RF predictions and the SPY returns
test_returns = np.sum(returns_monthly.iloc[train_size:] * test_predictions, axis=1)
plt.plot(test_returns, label='algo')


# Evaluate returns
# Let's now see how our portfolio selection would perform as compared with just investing in the SPY.
# We'll do this to see if our predictions are promising, despite the low R2 value.
#
# We will set a starting value for our investment of $1000, then loop through the returns from our predictions as well
# as from SPY. We'll use the monthly returns from our portfolio selection and SPY and apply them to our
# starting cash balance. From this we will get a month-by-month picture of how our investment is doing,
# and we can see how our predictions did overall vs the SPY. Next, we can plot our portfolio from our predictions
# and compare it to SPY.

# Calculate the effect of our portfolio selection on a hypothetical $1k investment
cash = 1000
algo_cash, spy_cash = [cash], [cash]  # set equal starting cash amounts
for r in test_returns:
    cash *= 1 + r
    algo_cash.append(cash)

# Calculate performance for SPY
cash = 1000  # reset cash amount
for r in returns_monthly['SPY'].iloc[train_size:]:
    cash *= 1 + r
    spy_cash.append(cash)

print('algo returns:', (algo_cash[-1] - algo_cash[0]) / algo_cash[0])
print('SPY returns:', (spy_cash[-1] - spy_cash[0]) / spy_cash[0])

# Plot the algo_cash and spy_cash to compare overall returns
plt.plot(algo_cash, label='ALGO')
plt.plot(spy_cash, label='SPY')
plt.legend()  # show the legend
plt.show()