from datacamp.machine_learning.first import prep
import matplotlib.pyplot as plt
import talib
import seaborn as sns

df = prep.give_me_raw_data()
print(df.head())

feature_names = ['5d_close_pct']  # a list of the feature names for later

# Create moving averages and rsi for timeperiods of 14, 30, 50, and 200
for n in [14, 30, 50, 200]:
    # Create the moving average indicator and divide by Adj_Close
    df['ma' + str(n)] = talib.SMA(df['Adj_Close'].values, timeperiod=n) / df['Adj_Close']
    # Create the RSI indicator
    df['rsi' + str(n)] = talib.RSI(df['Adj_Close'].values, timeperiod=n)

    # Add rsi and moving average to the feature name list
    feature_names = feature_names + ['ma' + str(n), 'rsi' + str(n)]


def give_feature_names():
    return feature_names


print(feature_names)
df['ma50'].plot()
df['Adj_Close'].plot(secondary_y=True)
# plt.show()


df = prep.give_processed_data()
# Drop all na values
lng_df = df.dropna()

# Create features and targets -- use the variable feature_names
features = lng_df[feature_names]
targets = lng_df['5d_close_future_pct']

# Create DataFrame from target column and feature columns
feat_targ_df = lng_df[['5d_close_future_pct'] + feature_names]

# Calculate correlation matrix
corr = feat_targ_df.corr()
sns.heatmap(corr)
print(corr)

# Plot heatmap of correlation matrix
sns.heatmap(corr, annot=True)
plt.yticks(rotation=0); plt.xticks(rotation=90)  # fix ticklabel directions
plt.tight_layout()  # fits plot area to the plot, "tightly"
# plt.show()  # show the plot
plt.clf()  # clear the plot area

# Create a scatter plot of the most highly correlated variable with the target
plt.scatter(lng_df['ma200'], lng_df['5d_close_future_pct'])
# plt.show()


def give_lng_df():
    return lng_df


def give_me_features():
    return features


def give_me_targets():
    return targets


def give_me_features_and_targets():
    return features, targets


