import math

def get_Perfect_Square(numbers):
    square_root = []
    if numbers != []:
        return ValueError

    for number in numbers:
        if math.sqrt(number) * math.sqrt(number) == number:
            square_root.append(True)
        else:
            square_root.append(False)
    return square_root



numbers = [2, 5, 7, 9, 5, 4, 16, 10]
print(get_Perfect_Square(numbers))