def get_maximum_In(my_list):

	maximum = my_list[0]

	for index in my_list:
		if index > maximum:
			maximum = index

	return maximum


def get_minimum_In(numbers):

	minimum = numbers[0]

	for index in numbers:

		if index < minimum:
			minimum = index


	return minimum

def get_sum_Of(values):

	sum = 0;

	for index in values:
		sum += index
	
	return sum

	if sum != sum:
		return 'ValueError'


def get_sum_Of_Even_Numbers_In(values):
	sumOfEven = 0;

	for numbers in values:
		if numbers % 2 == 0:
			sumOfEven += numbers

	return sumOfEven



def get_sum_Of_Odd_Numbers_In(values):
	sumOfOdd = 0;

	for numbers in values:
		if numbers % 2 != 0:
			sumOfOdd += numbers

	return sumOfOdd


def get_maximum_And_Minimum_Of(values):

	maximum = values[0]
	minimum = values[0]

	for numbers in values:
		if numbers > maximum:
			maximum = numbers
			
		if numbers < minimum:
			minimum = numbers

		maxmin = [maximum, minimum]
	
	return maxmin


