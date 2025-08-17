"""First function: Using a loop collect score from a user. Ensure the score is not less than zero nor graeter than 100. The function should return the score.
Second Function: Put grades into different score ranges (without showing the maximum)then use a multiple selection statement to compare between score and grade.
Each selection statement should return a grade. If score is from 80 to 100 A is assigned; 70 to 79 B is assigned, 50 to 69 C is assigned, 40 to 49 D is assigned
otherwise E is assigned.
Third Function: Also use multiple selection to assign comments to each grade: if grade is equal to A, the comment should be An Excellent performance
B the comment should be Good job, keep improving; C the comment should be Fair effort, keep working on it; D the comment should be You can do better, don't give up.
othrewise the comment should be Needs Improvement, Ask for help.
Each selection statement should return a comment for a particular grade.
Function four: Arrange all the functions into another function: assign the first function to a variable score since 
the first function will return the argument for the second function. Assign the second function to variable grade since 
the it returns the argument for the third function.
Then the second function and third should be printed. 
Ensure you ask the user at the end of getting a printing the third function if he wants to perform another check, 
therefore use loop inside the fourth function. If the user response is yes the fourth function executes again while if it is no, the loop terminates.
Ensure to make the user response not to be case sensitive.
"""




def get_score():
	score = int(input("Enter your score: "))
	while True:
		score = int(input("Enter your score: "))
		if score < 0 or score > 100:
			print("Invalid score. Please enter a score between 0 and 100.")
		else:	
			return score

def calculate_grade(score):
	if score >= 80:
		return "A"
	elif score >= 70:
		return "B"	
	elif score >= 50:
		return "C"
	elif score >= 40:
		return "D"
	else:
		return "E"

def get_feedback(grade):
	if grade == "A":
		return "An Excellent performance"
	elif grade == "B":
		return "Good job, keep improving"
	elif grade == "C":
		return "Fair effort, keep working on it"
	elif grade == "D":
		return "You can do better, don't give up."
	else:
		return "Needs Improvement, Ask for help."

def main():
	while True:
		score = get_score()
		grade = calculate_grade(score)
		print("Grade:", grade)
		print("Feedback:", get_feedback(grade))
		user_response = input("Try another score?(Yes/No):")
		if user_response.lower() == "no":
			break
		 
		
	
	
	
	
main()
	
	
	
	
	
	
	
	
