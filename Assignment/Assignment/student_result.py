
passes = 0
failures = 0

for students in range(10):
	result = int(input("enter 1 for pass, 2 for fail: "))

	if result == 1:
		passes += 1

	else: result == 2:
		failures += 1

	elif result != 1 or result != 2:
		result = int(input("wrong input,enter 1 for pass, 2 for fail: "))
	

print(f"passed students are: {passes}")
print(f"failed students are: {failures}")




