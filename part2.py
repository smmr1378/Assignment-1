print("welcome little student")
a = float(input("Enter the first side: "))
b = float(input("Enter the seconde side: "))
c = float(input("Enter the third side: "))
triangle = a + b + c
print(triangle)
if a > b + c or b > a + c or c > a + b:
    result = "a triangle is not formed"
else:
    result = "a triangle is formed"
print(result)