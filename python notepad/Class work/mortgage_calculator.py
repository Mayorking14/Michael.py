#collect requirments from user

principal = int(input('enter amount to borrow: '))

rate = input('enter interest rate in year: ')
rate = int(rate)

duration = input('enter years of mortgage: ')
duration = int(duration)

PERCENTAGE = 100
MONTHS = 12
NUM = 1

monthly_rate = (rate / PERCENTAGE) * MONTHS
no_of_month = duration * MONTHS

upper_equation = monthly_rate * ((NUM + monthly_rate) ** no_of_month)

lower_equation = (NUM + monthly_rate) ** no_of_month - NUM

monthly_payment = principal * (upper_eq / lower_eq)

print('Monthly payment is: ' , monthly_payment)


