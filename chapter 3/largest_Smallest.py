largest = 0
second_Largest = 0


for value in range(10):
	numbers = int(input("Enter number: "))
for number in numbers:
	if number > numbers:
		largest = number
	if number < largest and number > numbers:
		second_Largest = number

print(f'Largest is {largest}')
print(f'Second largest is {second_Largest}')