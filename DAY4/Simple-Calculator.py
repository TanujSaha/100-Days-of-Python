num1 = float(input("Enter number 1:"))
num2 = float(input("Enter number 2:"))

operator = input("Choose a Operator (+ , - , * , /):")

if operator == "+" :
    print(f"Sum of {num1} and {num2} = ", num1 + num2)
elif operator == "-" :
    print(f"Difference of {num1} and {num2} = ", num1 - num2)
elif operator == "*" :
    print(f"Multiplication of {num1} and {num2} = ", num1 * num2)
elif operator == "/" :
    print(f"Division of {num1} and {num2} = ", num1 / num2)
else:
    print("Invalid Input")


