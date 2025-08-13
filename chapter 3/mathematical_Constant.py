sum = 1
factorial = 1
for factor in range(1, 11):	
	factorial = factorial * factor
	sum = sum +(1 / factorial)
print(f'{sum}: .4f')
