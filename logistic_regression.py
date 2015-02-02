import pandas as pd
import statsmodels.api as sm
import math


#data cleaning
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#lambda function to an interest rate value and format to 4 d.p.
y = lambda x:round(float(x.rstrip('%'))/100,4)
#create a new clean interest rate colummn
loansData['Clean.Interest.Rate'] = loansData['Interest.Rate'].map(y)

z = lambda x: int(x.rstrip('months'))
loansData['Clean.Loan.Length'] = loansData['Loan.Length'].map(z)

#take first value of the fico score
loansData['Clean.FICO.Score'] = loansData['FICO.Range'].map(lambda x:int(x[:3]))
loansData['lt12.Interest.Rate'] = loansData['Clean.Interest.Rate'].map(lambda x:x<0.12)
loansData['Intercept'] = 1.0


def logistic_function(fico, amount):
	ind_vars = ['Intercept','Clean.FICO.Score','Amount.Requested']

	logit = sm.Logit(loansData['lt12.Interest.Rate'], loansData[ind_vars])
	result = logit.fit()
	coeff = result.params 

	p = 1.0/(1.0 + math.exp(coeff[ind_vars][0]+coeff[ind_vars][1]*fico+coeff[ind_vars][2]*amount)) 
	return p

# check to see if probabilities go down as fioo score goes up
for i in range(700,800,5):
	p = logistic_function(i,10000)
	print p

# check to see likelihood of this loan getting approved - answer 0.25 thus no
print logistic_function(720,10000)