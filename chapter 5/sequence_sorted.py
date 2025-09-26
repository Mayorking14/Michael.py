def is_ordered(sequence):
    for number in range(len(sequence)- 1):
        if sequence[number] > sequence[number + 1]:
            return False
    return True

sorted_list = [1, 2, 3, 4, 5]
print(is_ordered(sorted_list))

unsorted_list = [4, 5, 3, 2, 1]
print(is_ordered(unsorted_list))

sorted_tuple = (1, 2, 3, 4, 5)
print(is_ordered(sorted_tuple))

unsorted_tuple = (4, 5, 3, 2, 1)
print(is_ordered(unsorted_tuple))
