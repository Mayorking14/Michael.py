#2.10)
#(Arithmetic, Smallest and Largest) Write a script that inputs three integers #from #the user. Display the sum, average, product, smallest and largest of the #numbers. #sNote that each of these is a reduction in functional-style programming. 
#Ans:

number1 = input('enter integer: ')
number2 = input('enter integer: ')
number3 = input('enter integer: ')

sum = number1 + number2 + number3
print('Sum is' , sum)

sum = int(sum)
average = sum / 2
print("Average is" , average)

product = number1 * number2 * number3
product = int(product)
print("Product is" , product)

largest = number1
if number2 > largest:
  largest = number2
if number3 > largest:
  largest = number3
print('Largest is' , largest)

smallest = number1
if number2 < largest:
  smallest = number2
if number3 < largest:
  smallest = number3
print('Smallest is', smallest)
