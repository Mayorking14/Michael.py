def sum_innerList(num_list):
	new = []
	for index, number in enumerate(num_list):
		if num_list[index] == num_list[index]:
			new.append(sum(num_list[index])) 
	return new




input = [[2, 3, 4], [1, 5, 7], [4, 6, 8]]
print(sum_innerList(input))