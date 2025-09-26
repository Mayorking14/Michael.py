numbers = [1,2,3,4,5,6,7,8,9,10]

even_numbers = list(filter(lambda number: number % 2 == 0, numbers))
triple_of_even_numbers = list(map(lambda number: number * 3, even_numbers))

print(even_numbers)
print(triple_of_even_numbers)
print(sum(triple_of_even_numbers))