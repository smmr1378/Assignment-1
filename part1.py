import math

print("Welcome to RZ calculator")

print("+ : sum")
print("- : sub")
print("* : mul")
print("/ : div")
print("sin")
print("cos")
print("tan")
print("cot")
print("log")
print("sqrt")
print("factorial")
print("please enter your choice: ")
op = input()
if op == "+" or op == "-" or op == "*" or op == "/":
    a = float(input("enter first number: "))
    b = float(input("enter second number: "))
elif op == "factorial":
    a = int(input("enter first number: "))
else:
    a = float(input("enter first number:  "))

if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/":
    if b == 0:
        result = "cannot divide by zero"
    else:
        result = a / b
if op == "sin":
    result = (math.sin(a) * math.pi) / 180
elif op == "cos":
    result = (math.cos(a) * math.pi) / 180
elif op == "tan":
    result = (math.tan(a) * math.pi) / 180
elif op == "cot":
    result = 1 / (math.tan(a) * math.pi) / 180
elif op == "log":
    result = math.log(a)
elif op == "sqrt":
    if a < 0:
        result = "cannot divide by zero"
    else:
        result = math.sqrt(a)
elif op == "factorial":
    result = math.factorial
    

        
print(result)
