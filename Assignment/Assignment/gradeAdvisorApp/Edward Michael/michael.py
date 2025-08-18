#firstly create a function that takes student score input within 0 and 100
#create another function that does calculate  the score and determine the grade
#and then assign a feedback to each grade based on the score, that in another function too
#create a function that contains all of these functions
#lastly prompt an option to retry if they are willing or not




def get_score():
	while True:
		score = int(input("Enter the student's score (0 - 100): "))
		if score < 0 or score > 100:
			print("Invalid, score must be between 0 and 100.")
		else:
			return score

def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    elif score >= 50:
        return 'E'
    else:
        return 'F'

def get_feedback(grade):
	if grade == 'A':
		print("Excellent performance!")
	elif grade == 'B':
		print("Good performance!")
	elif grade == 'C':
		print("Fair effort, keep working on it.")
	elif grade == 'D':
		print("You can do better, don't give up.")
	elif grade == 'E':
		print("Needs improvement.")
	elif grade == 'F':
		print("Really needs improvement, seek help.")

def main():
	while True:
		score = get_score()
		grade = calculate_grade(score)
	
		print(f"\nGrade is {grade}")
		print(get_feedback(grade))
		
		retry_score = input("Do you want to enter another score? (yes/no): ")
		if retry_score != 'yes':
			break

main()
