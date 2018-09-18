import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
# Import statsmodels.formula.api

FamaFrenchData = pd.read_csv('resources/FamaFrenchFactors.csv')

# Calculate excess portfolio returns
FamaFrenchData['Portfolio_Excess'] = FamaFrenchData['Portfolio'] - FamaFrenchData['RF']

# Plot returns vs excess returns
CumulativeReturns = ((1+FamaFrenchData[['Portfolio','Portfolio_Excess']]).cumprod()-1)
CumulativeReturns.plot()
plt.show()

# Calculate the co-variance matrix between Portfolio_Excess and Market_Excess
covariance_matrix = FamaFrenchData[['Portfolio_Excess', 'Market_Excess']].cov()
# Extract the co-variance co-efficient
covariance_coefficient = covariance_matrix.iloc[0, 1]
print(covariance_coefficient)



# Define the regression formula
CAPM_model = smf.ols(formula="Portfolio_Excess ~ Market_Excess", data=FamaFrenchData)

# Print adjusted r-squared of the fitted regression
CAPM_fit = CAPM_model.fit()
print(CAPM_fit.rsquared_adj)

# Extract the beta
regression_beta = CAPM_fit.params["Market_Excess"]
print(regression_beta)


# Multifactor
# Define the regression formula
FamaFrench_model = smf.ols(formula='Portfolio_Excess ~ Market_Excess + SMB + HML', data=FamaFrenchData)
# Fit the regression
FamaFrench_fit = FamaFrench_model.fit()
# Extract the adjusted r-squared
regression_adj_rsq = FamaFrench_fit.rsquared_adj
print(regression_adj_rsq)



# Extract the p-value of the SMB factor
smb_pval = FamaFrench_fit.pvalues["SMB"]
# If the p-value is significant, print significant
if smb_pval < 0.05:
    significant_msg = 'significant'
else:
    significant_msg = 'not significant'

# Print the SMB coefficient
smb_coeff = FamaFrench_fit.params["SMB"]
print("The SMB coefficient is ", smb_coeff, " and is ", significant_msg)


# Calculate your portfolio alpha
portfolio_alpha = FamaFrench_fit.params["Intercept"]
print(portfolio_alpha)
# Annualize your portfolio alpha
portfolio_alpha_annualized = (1 + portfolio_alpha)**252 - 1
print(portfolio_alpha_annualized)


# Define the regression formula
FamaFrench5_model = smf.ols(formula='Portfolio_Excess ~ Market_Excess + SMB + HML + RMW + CMA ', data=FamaFrenchData)
# Fit the regression
FamaFrench5_fit = FamaFrench5_model.fit()
# Extract the adjusted r-squared
regression_adj_rsq = FamaFrench5_fit.rsquared_adj
print(regression_adj_rsq)