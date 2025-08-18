"""
prompt the user for input.
validate if input is between 0 and 100, if not give chance to run the program again.


"""
def get_score():
	user_score = int(input('Please enter a value between 0 and 100  :'))
	while user_score < 0 or user_score > 100:
		user_score = int(input('Invalid input: Please enter a value between 0 and 100 :'))
	return user_score
		
"""
use conditional statement to determine the grade of student.
"""
	
def calculate_grade(score):
	if score >= 90:
		return 'A'
	elif score >= 80:
		return  'B'
	elif score >= 70:
		return  'C'
	elif score >= 60:
		return  'D'
	else:
		return  'F'
		
"""
use conditional statement determine the feedback of the student.
"""
		
def get_feedback(grade):
	if grade == 'A':
		return 'Excellent performance'
	elif grade == 'B':
		return 'Good job, Keep improving'
	elif grade == 'C':
 		return 'Fair effort, keep working on it'
	elif grade == 'D':
		return 'You can do better, don’t give up'
	else:
		return 'Needs Improvement, Ask for help'
		
		
		
		
def main():
	score = get_score()
	grade = calculate_grade(score)
	print(grade)
	feedback = get_feedback(grade)
	print(feedback)
	user = input('Try another score? (yes/no)')
	while (user == 'yes'):
		score = get_score()
		grade = calculate_grade(score)
		print(grade)
		feedback = get_feedback(grade)
		print(feedback)
		user = input('Try another score? (yes/no)')



main()			
		
		
		
		
	