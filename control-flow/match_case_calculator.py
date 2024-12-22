# Prompt the user to enter two numbers and select an operation
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

# Perform the calculation using Match Case
result = match operation:
    case "+":
        num1 + num2
    case "-":
        num1 - num2
    case "*":
        num1 * num2
    case "/":
        if num2 != 0:
            num1 / num2
        else:
            "Cannot divide by zero."
    case _:
        "Invalid operation selected."

# Display the result of the operation
if isinstance(result, str):
    print(result)
else:
    print(f"The result is {result}.")