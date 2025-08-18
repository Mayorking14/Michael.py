""" A console program that calculates student grades and gives feedback
	I did this using the following steps:
	1. define a function that prompts user to enter score
	2. declare a while loop and an if statement inside the function to keep prompting user to enter the correct digit(0-100) 
	3. define another function to check for the hierrachy of grades(A-F)
	4. define another function to assign the right feedback for any grade
	5. define another function that runs the whole function(main function)
	6. declare a while loop inside the main function to keep prompting the user to check for another score """
	
def get_score():
	while True:
		user_score = float(input('Enter score(0-100):'))
		if user_score <= 0 or user_score > 100:
			print("Inavlid score")
		else:
			return user_score
			
			
def calculate_grade(user_score):
	if user_score >= 90:
		return 'A'
	elif user_score >= 70:
		return 'B'
	elif user_score >= 50:
		return 'C'
	elif user_score >= 40:
		return 'D'
	else:
		return 'F'
def get_feedback(grade):
	if grade == 'A':
		return 'Excellent performance'
	elif grade == 'B':
		return 'Good job,keep improving'
	elif grade == 'C':
		return 'Fair effort, keep working on it'
	elif grade == 'D':
		return 'You can do better, dont give up'
	else:
		return 'Needs improvement,ask for help'
def main():
	while True:
		user_score = get_score()
		grade = calculate_grade(user_score)
		feedback = get_feedback(grade)
		print('Your grade is',grade)
		print('My feedback for you is:', feedback)
		
		try_again = input('Wish to check for another score? press yes or press any number to quit: ')
		if try_again != 'yes':
			print("Thank you,bye")
			break
main() 
		
			
			