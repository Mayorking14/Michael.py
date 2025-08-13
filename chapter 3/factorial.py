num = int(input('enter a number: '))

if num < 0:
    print("invalid, input positive number.")
else:
    factorial = 1
    for digit in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}")