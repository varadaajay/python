def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero!"

# Main program loop
while True:
    # Take operator as input
    operator = input("Enter operator (+, -, *, /) or 'q' to quit: ")

    if operator == 'q':
        break

    if operator in ('+', '-', '*', '/'):
        # Take numbers as input
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if operator == '+':
            print(num1, "+", num2, "=", add(num1, num2))

        elif operator == '-':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif operator == '*':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif operator == '/':
            print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Invalid operator. Please try again.")
