num = list(range(1,21))
def filter_Even(num):
	return num % 2 == 0
	
	 
print(list(filter(filter_Even,num)))