import math
def get_divide_or_square(number):
	if type(number) == str:
		return 'ValueError'
	
	elif type(number) == chr:
		return 'ValueError'
	
	elif (number % 5 == 0):
		return math.sqrt(number)
	
	elif (number % 5 != 0):
		return number % 5

	elif (number < 0):
		return 'invalid'
		
	


def get_future_investment_value(investment_amount, monthly_interest_rate, years):	

	numberOfMonths = years * 12

	get_future_investment_value = investment_amount * (1 + monthly_interest_rate) ** numberOfMonths
	

	if (investment_amount) == str:
		return 'ValueError'

	elif (years) == float:
		return 'ValueError'
	
	elif (monthly_interest_rate) < 0:
		return 'ValueError'
	
	elif (get_future_investment_value != investment_amount * (1 + monthly_interest_rate) ** numberOfMonths):
		return 'ValueError'
		
		