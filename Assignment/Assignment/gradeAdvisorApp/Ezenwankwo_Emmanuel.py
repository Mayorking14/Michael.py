"""This is an app that calculates the scores of students, it calculates their grade, and gives performance feedback.

for the first function, break score into test and exam score.
collect an input for test and for exam score. 
use loop to ensure student input tallies with specified range of scores.
add the test and exam scores in a total variable
print result of scores and the result of total

for function two,call the return value of function one into calculate_grade.
check if total is greater than or equals to various set values.
print value of grade and also return grade

for function three, check for each grade and print approprait feed back.
add emoji for extra beauty.

for the final step, store my fucntions in a variable
call main() 
"""


def get_score():
    while True:
        test_score = int(input("Enter your test score (0-30): "))
        if 0 <= test_score <= 30:
            break
        else:
            print("This is an incorrect test score. Please enter a number within 0 and 30: ")

    while True:
        exam_score = int(input("Enter your exam score (0-70): "))
        if 0 <= exam_score <= 70:
            break
        else:
            print("This is an incorrect exam score. Please enter a number within 0 and 70: ")

   
    total = test_score + exam_score
    print(f"\nHaving scored {test_score} in your test and scoring {exam_score} in your exam")
    print(f"Your total score is {total}") 
    return total


def calculate_grade(total):
    if total >= 70:
        grade = 'A'
    elif total >= 60:
        grade = 'B'
    elif total >= 50:
        grade = 'C'
    elif total >= 45:
        grade = 'D'
    elif total >= 40:
        grade = 'E'
    else:
        grade = 'F'
    print(f"And your grade is: {grade}")
    return grade


#Got my emoji from emojicomobs.com 😉
def get_feedback(grade):
    if grade == 'A':
        print("You had an excellent performance! Keep it up. 🙌🥳🎊")
    elif grade == 'B':
        print("Good job, keep improving! 😊👌")
    elif grade == 'C':
        print("Impressive! there is room for improvement 🤒⃕😊👌")
    elif grade == 'D':
        print("You can do better-keep studying! 💻⋆⭒˚☕️｡⋆")
    elif grade == 'E':
        print("Poor performance-keep studing! ✧💻☕📝")
    else:
        print("You failed. Please attend classes!! ❌📉")




def main():
    while True:
        total = get_score()   
        grade = calculate_grade(total)
        get_feedback(grade)

        try_again = input("\nDo you want to calculate another student's score? (Yes/No): ").strip().lower()

        if try_again != 'yes':
            print("Thank you for using my app, Goodbye!")
            break

main()

