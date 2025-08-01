number1 = int(input('enter a number: '))
number2 = int(input('enter a number: '))
number3 = int(input('enter a number: '))

sum_total = number1 + number2 + number3
print('Sum is: ',sum_total)

average = sum_total / 3
print('Average is: ',average)

product = number1 * number2 * number3
print('Product is: ',product)

smallest = number1

if number2 < smallest:
	smallest = number2

elif number3 < smallest:
	smallest = number3
print('Smallest is: ',smallest)

largest = number1

if number2 > largest and number2 > number3:
	largest = number2

elif number3 > largest and  number3 > number2:
	largest = number3

print('Largest is: ',largest)
