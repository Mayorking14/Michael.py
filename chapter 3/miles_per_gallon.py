total_Miles = 0
total_Gallons = 0

miles = int(input("Enter miles, -1 to end: "))
gallons = int(input("Enter gallons, -1 to end: "))

while miles != -1:
	total_Miles += miles
	total_Gallons += gallons
	miles = int(input("Enter miles, -1 to end: "))
	gallons = int(input("Enter gallons, -1 to end: "))


if total_Miles != 0:
	total_Miles_Per_Gallon = total_Miles / total_Gallons
print(f'Total miles driven per gallon is {total_Miles_Per_Gallon}')



