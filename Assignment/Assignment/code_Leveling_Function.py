
def add_tuple(number, number2):
	for check in number:
		if type(check) != type(2):
			raise  ValueError
		else:
			return (number  + number2 )

number = (2,1,5,6,8,4,67)
number2 = (7,9,23,54)
result = add_tuple(number, number2)
print(result)


def changing_value(numbers):
	numbers = (1, 2, [3, 4], 5)
	numbers[2][1] = 99
	return numbers
	
numbers =  (1, 2, [3, 4], 5)
numbers[2][1] = 99
result = changing_value(numbers)
print(result)
	
def convert_tuple_of_strings(tuple):
	words = ('apple', 'banana', 'cherry')
	new_word = list(words)
	new_word.append('mango')
	words = tuple(words)
	return words


def unpacking_tuples(digit):
	digit = (10, 20, 30, 40)
	a, b, *others = digit
	print(a, b, others)
	

def summing_rows_of_2Dlist(digit):
	array_list = []
	for index in range(3):
		sum =  0
		for count in range(3):
			sum += digit[index][count]
		array_list.append(sum)	
	return array_list
	
digit =  [ [2, 3, 4], [1, 5, 7], [4, 6, 8] ]
result = summing_rows_of_2Dlist(digit)
print(result)
	


def summing_columns_of_2Dlist(digit):
	array_list= []
	for index in range(3):
		sum =  0
		for count in range(3):
			sum += digit[count][index]
		array_list.append(sum)	
	return array_list
					
digit =  [ [2, 3, 4], [1, 5, 7], [4, 6, 8] ]
result = summing_columns_of_2Dlist(digit)
print(result)





num = list(range(1,21))
def get_all_even_numbers(digit):
	return digit % 2  == 0
		
print(list(filter(get_all_even_numbers, num)))


def extract_long_words(words):
	extracted_word = []
	for word in words:
		if(len(word) > 5):
			extracted_word.append(word)
	return extracted_word
	
	
word = ['cat','elephant', 'tiger', 'lion']
result = extract_long_words(word)
print(result)




tuples= [(1, 'A'), (4, 'B'), (2, 'C')]
def is_greater_than_two (digit):  
    return digit[0] > 2
filtered = list(filter(is_greater_than_2, tuples))
print(filtered)



def is_divisible_by_three_and_five(num):
    return num % 3 == 0 and num % 5 == 0

divisible_numbers = list(filter(divisible_by_3_and_5, range(1, 51)))
print(divisible_numbers)



def is_palindrome(word):
    return word == word[ : :-1]
   
words = ['level', 'world', 'madam', 'python','tundednut']
palindromes = list(filter(is_palindrome, words))
print(palindromes)



def do_strings_to_upper_case(word):
	upper_case = list(map(str.upper, word))
	return upper_case


word = ['python', 'java', 'c++']
result = do_strings_to_upper_case(word)
print(result)

def square_function(number):
	return number ** 2


def to_square_all_numbers(digit):
	squared_list = list(map(square_function, digit))
	return squared_list
	
number = range(1,11)
result = to_square_all_numbers(number)
print(result)

def capital_letter(word):
	capital_letter = list(map(str.capitalize,word))
	return capital_letter
	

word = ['python', 'java', 'c++']
result = capital_letter(word)
print(result)

def tax_percentage(number):
	return number + number * 0.1

def add_tax_to_all_list(digit):
	added_tax = list(map(tax_percentage, digit))
	return added_tax
	
	
digit = [100, 200, 300]
result = add_tax_to_all_list(digit)
print(result)
	



from functools import reduce		
def addition(digit1, digit2):
	return digit1 + digit2
	
digit = range(1,51)
summation = reduce(addition, digit)
print(summation)	
	


from functools import reduce
def max_number(digit1, digit2):
	if digit2 > digit1:
		return digit2
	else: 
		return digit1
		
		
number = [ 3, 5, 9, 2, 8]
result = reduce(max_number, number)
print(result)




from functools import reduce
def max_number(digit1, digit2):
	if digit2 > digit1:
		return digit2
	else: 
		return digit1
		
		
number = [ 3, 5, 9, 2, 8]
result = reduce(max_number, number)
print(result)




from functools import reduce
def concatenate_letters(word1, word2):
	return word1 + " " + word2		
		
word = ['I', 'love', 'Python']
result = reduce(concatenate_letters, word)
print(result)





def square_function2(number):
	return number ** 2


def square_all_numbers(digit):
	squared = list(map(square_function2, digit))
	return squared

number = range(1, 5)
result = square_all_numbers(number)
print(result)
	
	

from functools import reduce
def number_squared(digit1, digit2):
	return digit1 * digit2
	
		
number = range(1,5)
result = reduce(number_squared, number)
print(result)
	

def list_of_tuples(digit):
	new_digit = []

	digit = [(1,2) , (2,4), (5,2)]
	tuple_convert_to_list	= [sum([1,2]), sum([2,4]), sum([5,2])]
	return tuple_convert_to_list
	


digit = [(1,2) , (2,4), (5,2)]
result = list_of_tuples(digit)
print (result)
	
	
def add(x, y):
	return x + y
	
	digit = [(1, 2), (3, 4), (5,6)]
	tuple_convert_to_list = [add(1,2), add(2,4), add(5,2)]
	return tuple_convert_to_list


#result = add( [(1,2) , (2,4), (5,2)])
#print (result)
# wrong output.



	
def get_words_number_five(digit):
	if (digit > 5):
		return digit
	
digit = [sum([1,2]), sum([2,4]), sum([5,2])]
def get_filter_number(digit):
	filtered = list(filter(get_words_number_five, digit))
	return filtered
	
	
digit = [sum([1,2]), sum([2,4]), sum([5,2])]
result = 	get_filter_number(digit)
print(result)

def check_non_integer(digit):
	if (str.isdigit(digit)):
		return digit
		
def integer(digit):
	filtered = list(filter(check_non_integer, digit))
	
	return filtered
	
	
digit =  ['123', '456', '789', 'abc', 'def']
result =  integer(digit)
print(result)



def convert_string_to_integer(result):
	integer = list(map(int, result))
	return integer

numbers = ['123', '456', '789']
result = convert_string_to_integer(numbers)
print(result)


	
from functools import reduce
def sum_integer(digit1, digit2):
	return digit1 + digit2
	
		
number =  convert_string_to_integer(numbers)
result = reduce(sum_integer, number)
print(result)