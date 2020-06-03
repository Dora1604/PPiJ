
## line plot of time series
#from pandas import read_csv
#from matplotlib import pyplot
## load dataset
#series = read_csv('daily-minimum-temperatures.csv', header=0, index_col=0)
## display first few rows
#print(series.head(20))
## line plot of dataset
#series.plot()
#pyplot.show()

# split the dataset
from pandas import read_csv
series = read_csv('daily-minimum-temperatures.csv', header=0, index_col=0)
split_point = len(series) - 7
dataset, validation = series[0:split_point], series[split_point:]
print('Dataset %d, Validation %d' % (len(dataset), len(validation)))
dataset.to_csv('dataset.csv', index=False)
validation.to_csv('validation.csv', index=False)


# create a differenced series
def difference(dataset, interval=1):
	diff = list()
	for i in range(interval, len(dataset)):
		value = dataset[i] - dataset[i - interval]
		diff.append(value)
	return numpy.array(diff)

# create a differenced series
def difference(dataset, interval=1):
	diff = list()
	for i in range(interval, len(dataset)):
		value = dataset[i] - dataset[i - interval]
		diff.append(value)
	return numpy.array(diff)

# invert differenced value
def inverse_difference(history, yhat, interval=1):
	return yhat + history[-interval]

