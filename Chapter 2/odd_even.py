#2.6)
# (Odd or Even) Use if statements to determine whether an integer is odd or even.
# [Hint: Use the remainder operator. An even number is a multiple of 2. Any multiple of 2 leaves a remainder of 0 when divided by 2.]
#Ans:
number = input('Enter integer: ')
number = int(number)

if number % 2 == 0:
   print('its an even number')

if number % 2 != 0:
    print ('its an odd number')