#1. I created a function to get a student score
#2. i prompt the user to enter a score .
#3. i checked if the score is greater than 100
#4. If the score is invalid it will print "invalid score must be between 0 and 100".
#5. If the score is valid, return the score.

def get_score():
	score = float(input("Enter student score:"))
	if (score > 100 ):
		print("invalid score must be between 0 and 100")
	else:
		return score



#1. I created a function to get a calculate student grade.
#3. i checked if the score is greater than and equals to 70 it will return "A"
#3. i checked if the score is greater than and equals to 60 it will return "B"
#4. i checked if the score is greater than and equals to 50 it will return "C"
#5. i checked if the score is greater than and equals to 45 it will return "D"
#6. i checked if the score is greater than and equals to 40 it will return "E"
#3. else return "F"



def calculate_grade(score):
	if (score >= 70):
		return "A"
	if (score >= 60):
		return "B"
	if (score >= 50):
		return "C"
	if (score >= 45 ):
		return "D"
	if (score >= 40):
		return "E"
	else:
		return "F"



#1. I created a function to get a calculate get feedback.
#2. if the grade is   equals to "A" it will return "Excellent performance"
#3. if the grade is   equals to "B" it will return "Good job, keep improving"
#4. if the grade is   equals to "C" it will return "You can do better, don't give up"
#5. if the grade is   equals to "D" it will return "Don't give up"
#5. if the grade is   equals to "E" it will return "Needs improvement"
#5. if the grade is   equals to "F" it will return "Scream for help"




def get_feedback(grade):
	if (grade == "A"):
		return "Excellent performance"
	if (grade == "B"):
		return "Good job, keep improving"
	if (grade == "C"):
		return "You can do better, don't give up"
	if (grade == "D"):
		return "don't give up"
	if (grade == "E"):
		return "Needs improvement"
	if (grade == "F"):
		return "Scream for help"
		

	



score = get_score()
calculate_grade(score)
print(calculate_grade(score))
grade = calculate_grade(score)
print(get_feedback(grade))