import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#lambda function to an interest rate value and format to 4 d.p.
y = lambda x:round(float(x.rstrip('%'))/100,4)
#create a new clean interest rate colummn
loansData['Clean.Interest.Rate'] = loansData['Interest.Rate'].map(y)


z = lambda x: int(x.rstrip('months'))
loansData['Clean.Loan.Length'] = loansData['Loan.Length'].map(z)

#take first value of the fico score
loansData['Clean.FICO.Score'] = loansData['FICO.Range'].map(lambda x:int(x[:3]))

#plt.figure()
#p = loansData['Clean.FICO.Score'].hist()
#plt.show()

#plt.figure()
#a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')
#plt.show()

intrate = loansData['Clean.Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['Clean.FICO.Score']

# The dependent variable
y = np.matrix(intrate).transpose()
# The independent variables shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

x = np.column_stack([x1,x2])

X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

print 'Coefficients: ', f.params[0:2]
print 'Intercept: ', f.params[2]
print 'P-Values: ', f.pvalues
print 'R-Squared: ', f.rsquared
