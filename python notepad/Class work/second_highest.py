x = 42

y = 12

z = 55

largest = x

if (y > largest and y > z):
	largest = y

if (z > largest and z > y):
	largest = z


if (x < largest and x > y):
	second_largest = x

elif (y < largest and y > x):
	second_largest = y

print(f"Second largest is {second_largest}")
