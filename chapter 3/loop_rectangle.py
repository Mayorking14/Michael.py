count = 0
while count < 11
	star = 0
	while star <= count:
		print('t', end='')
		star += 1

	space = 11
	while space > count:
		print('p', end='')
		space -= 1
	count += 1
	print()