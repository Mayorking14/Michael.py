square = 1
cube = 0

print(f'numbers\t square\t  cube')
for numbers in range(6):
	square = numbers**2
	cube = numbers**3
	print(f'{numbers:>6}\t {square:>6}\t {cube:>6}')