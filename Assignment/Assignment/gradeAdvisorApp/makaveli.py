def get_score() :
	while True :
		score = int(input("Enter student score:  "))
		if score <= 100 :
			return score
		else :
			print("Invalid score. Please enter a value between 0 and 100")


def calculate_score(score) :
	if score >=90 :
		grade = "A"
	elif score >= 75 :
		grade = "B"
	elif score >= 55 :
		grade = "C"
	elif score >= 35 :
		grade = "D"
	else :
		grade= "F"
	print("Grade: ", grade)
	return grade

def get_feedback(Grade) :
	if Grade == "A" :
		print("Excelent job!")
	elif Grade == "B" :
		print("Awesome")
	elif Grade == "C" :
		print("You can do better!")
	elif Grade == "D" :
		print("Nur try this next semester o!")
	else :
		print("Dey go house!!!")

def main() :
	while True :
		score = get_score()
		grade = calculate_score(score)
		get_feedback(grade)
		answer = str(input("Do you want to continue (Yes/No):  "))
		if answer == "No" or answer == "no" or answer == "NO" :
			break
main()
