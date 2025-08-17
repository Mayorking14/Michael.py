def get_score() :
	user_input = int(input("Enter Student Score\n"))
	while user_input < 0 or user_input > 100 : 
		print("Invalid Score , Enter a valid Score Between 0 and 100")
		user_input = int(input("Enter Student Score\n"))
	return user_input

def calculate_grade(score) :
	if(score > 85) : grade = 'A'
	elif(score< 85 and score >= 75) : grade = 'B'
	elif(score < 75 and score >= 60) : grade = 'C'
	elif(score < 60 and score >= 45) : grade = 'D'
	elif(score < 45 and score >= 30) : grade = 'E'
	else : grade = ' Grade : F'
	return grade

def feedback(grade):
	if  grade == 'A' : print("Excellent Performannce")
	elif grade == 'B' : print("Good Job,Keep Improving")
	elif grade == 'C' : print("Fair Effort, Keep working on it")
	elif grade == 'D' : print("You Can do a better job, don't give up")
	elif grade == 'E' : print("Need Improvement, Ask For Help")
	else : print("You No Know Book Leave School You are ment to be a cleaner")

def main():
	get_grade = get_score()
	grade_response = calculate_grade(get_grade)
	print(f"Grade : {grade_response}")
	feedback(grade_response)
main()

user_continuation_response = input("Try Another Score (yes/no)\n")
while user_continuation_response == "yes" :
	main()
	user_continuation_response = input("Try Another Score (yes/no)\n")
	
	
		
	
	
	