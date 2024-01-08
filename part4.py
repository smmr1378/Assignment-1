print("BMI")

weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))
bmi = weight / (height ** 2)
print(bmi)

if bmi < 18.5:
    result = "Underweight"
elif 18.5 <= bmi < 24.9:
    result = "Normal weight"
elif 25 <= bmi < 29.9:
    result = "Overweight"
elif 30 <= bmi < 34.9:
    result = "Obesity"
elif 35 <= bmi < 39.9:
    result = "Extreme Obesity"
else:
    result = "Invalid BMI"

print(result)