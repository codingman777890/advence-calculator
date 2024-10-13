print("Welcome to caculator")
print("select an operator")
print("1. Addition", "+")
print("2. Subtraction", "-")
print("3. Multiplication", "*")
print("4. Division", "/")


operator = input("Enter the operator (+, -, *, /): ")
num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))

if operator == "+":
    print("The number is ", num1 + num2)
elif operator == "-":
    print("The number is ", num1 - num2)
elif operator == "*":
    print("The number is ", num1 * num2)
elif operator == "/":
 if num2 == 0:
    print( "Error: Division by zero" )
else:
    print("The number is ", num1 / num2)
