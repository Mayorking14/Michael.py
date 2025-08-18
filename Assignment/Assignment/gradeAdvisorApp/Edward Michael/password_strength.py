

#Prompts and user to input a password
#create a function that checks for the complexity of the password by counting number of alphabet and numbers using a loop.
#creating another function that evaluates and returns the password strength using the selection statements
#putting all of the above functions in a main function
#lastly, prompting if the user would like to input another password 	




def get_password():
	password = input("Enter your password: ")

def check_complexity(password):
	alphabet_count = 0
	for char in password:
		if char.isalpha():
			alphabet_count += 1
	return alphabet_count

	number_count = 0
	for char in password:
		if char.isdigit():
			number_count += 1
	return number_count

def evaluate_strength(alphabet_count, number_count):
	total_length = alphabet_count + number_count

	if total_length < 6 or number_count == 0:
		return "Weak"
	elif 6 <= total_length <= 8 and number_count >= 1:
		return "Moderate"
	elif total_length > 8 and number_count >= 2:
		return "Strong"
	else:
		return "Weak"

def main():
	while True:
		password = get_password()
		alphabet_count = check_complexity(password)
		number_count = check_complexity(password)

		strength = evaluate_strength(alphabet_count, number_count)
		print(f"Password Strength: {strength}")

		retry = input("Do you want to try another password? (yes/no): ").lower()
		if retry != 'yes':
                  break

main()