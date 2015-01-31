import pandas as pd
from scipy import stats

data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''

# First, split the string on the (hidden characters that indicate) newlines
data = data.splitlines() # we could also do data.split('\n')

# Then, split each item in this list on the commas
# the bracketed expression is a list comprehension
data = [i.split(', ') for i in data] 

# Now, convert create a pandas dataframe
column_names = data[0] # this is the first row

data_rows = data[1::] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)

# Convert Alcohol and Tobacco columns to float
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

# mean median mode range variance standard deviation for tobacco and Alcohol
# dataset this is a bit weird as we have two different items in here
# so i have interpreted the question as looking at total spend on both
# leaving mode out as we dont have repeated items 
sinspend = (df['Alcohol']+df['Tobacco'])

print "The mean total alcohol and tobacco spend is {}".format(sinspend.mean())
print "The median total alcohol and tobacco spend is {}".format(sinspend.median())
#print "The mode of total alcohol and tobacco spend is {}".format(sinspend.mode())
print "The variance of total alcohol and tobacco spend is {}".format(sinspend.var())
print "The standard deviation of total alcohol and tobacco spend is {}".format(sinspend.std())
print "The range of total alcohol and tobacco spend is {}".format(max(sinspend)-min(sinspend))





