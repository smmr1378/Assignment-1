print("welcome")
print("Enter your name: ")
name = input()
print("Enter your last name: ")
lastname = input()
score1 = float(input("Enter the grade of the first lesson: "))
score2 = float(input("Enter the grade of the seconde lesson: "))
score3 = float(input("Enter the grade of the third lesson: "))

average = (score1 + score2 + score3) / 3

print(average)
if average >= 17:
    result = "great"
elif 17>average >12:
    result = "Normal"
elif average < 12:
    result = "Fail"

print(result)