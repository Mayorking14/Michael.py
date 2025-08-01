positive = "yes"
negative = "no" 

question1 = input("what's your problem ? : ")

question2 = input(str("Have you had this problem before(yes or no ?): "))

if question2 == positive:
	print('well, you have it again.')
elif question2 == negative:
	print('well, you have it now.')
