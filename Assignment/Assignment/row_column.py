for row in range(10):
	for column in range(10):
		print('<' if row % 2 == 1 else '>', end='')
	print()

#this will print '<' and '>' 10 times each