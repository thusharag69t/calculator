# A friendly, calculator

print("--- Hello! I am your personal calculator assistant. ---")

# Getting input from the user
num1 = float(input("Enter your first number: "))
operation = input("What would you like to do? (+, -, *, /): ")
num2 = float(input("Enter your second number: "))

# Logic to calculate the result
if operation == "+":
    result = num1 + num2
    word = "added to"
elif operation == "-":
    result = num1 - num2
    word = "minus"
elif operation == "*":
    result = num1 * num2
    word = "multiplied by"
elif operation == "/":
    if num2 == 0:
        result = "undefined (you can't divide by zero!)"
        word = "divided by"
    else:
        result = num1 / num2
        word = "divided by"
else:
    result = None
    print("Sorry, I didn't recognize that operation.")

# Printing the result
if result is not None:
    print(f"\nOkay! {num1} {word} {num2} is exactly: {result}")
    print("Have a great day!")
10