def list_Sum(numbers):
	new = []
	new_num = 0
	for num in numbers:
		new.append(sum(num))
		
	return new





input = [[2, 3, 4], [1, 5, 7], [4,6,8]]

print(list_Sum(input))