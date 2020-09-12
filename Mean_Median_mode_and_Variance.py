import statistics

def mmmv():
	i = [int(x) for x in input('Enter your numbers(seperate by spaces" "): ').split()]
	print('Mean:',statistics.mean(i))
	print('Median:',statistics.median(i))
	print('Variance:',statistics.variance(i))
	try:
		print('Mode:',statistics.mode(i))
	except statistics.StatisticsError as e:
		print(e)
mmmv()
'''
mean
median
mode
variance
'''