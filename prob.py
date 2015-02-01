import collections
import matplotlib.pyplot as plt
import numpy as np 
import scipy.stats as stats

def show_data(test_data, description):
	"""Displays a box plot, histogram and a QQ graph (based on normality), also prints some descriptive
	statistics"""

	#at the moment it also saves as .png files - however naming is not unique
	plt.figure()
	plt.title('Box Plot-'+description)
	plt.boxplot(test_data)
	plt.savefig("boxplot.png")
	plt.show()

	plt.figure()
	plt.title('Histogram-'+description)
	plt.hist((test_data),histtype='bar')
	plt.savefig("Histogram.png")
	plt.show()

	plt.figure()
	qq = stats.probplot(test_data, dist="norm", plot=plt)
	plt.savefig("QQ.png")
	plt.show()

	description = stats.describe(test_data)
	print "The number of observations is:{}".format(description[0])
	print "The minimum and max of the observations are :{} , {}".format(description[1][0],description[1][1])
	print "The mean of the observations is {}".format(description[2])
	print "The variance of the observations is {}".format(description[3])
	print "The skewness of the observations is {}".format(description[4])
	print "The normalised kurtosis of the observations is {}".format(description[5])

	freq_dump = stats.histogram(test_data,10)

	for i in range(10):
		bottom_range = freq_dump[1]+freq_dump[2]*i
		top_range = bottom_range + freq_dump[2]
		print "The proportion from {} to {} is {}".format(bottom_range,top_range,freq_dump[0][i]/len(test_data))


if __name__ == "__main__":

	#Test data - 1000, normal, uniform and cauchy variables
	test_data_n = np.random.normal(size=1000) 
	test_data_u = np.random.uniform(size=1000) 
	test_data_w = np.random.standard_cauchy(size=1000) 

	show_data(test_data_n," Normal variables")
	show_data(test_data_u," Uniform variables")
	show_data(test_data_w," Cauchy variables")