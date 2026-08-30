def calculator():
    print("=== Command-Line Calculator ===")
    print("Operators: +, -, *, /")
    print("Type 'exit' to quit.\n")

    while True:
        op = input("Enter operator (+, -, *, /) or 'exit': ").strip()
        if op.lower() == 'exit':
            print("Goodbye!")
            break

        if op not in ('+', '-', '*', '/'):
            print("Invalid operator! Try again.\n")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid number! Try again.\n")
            continue

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        else:
            if num2 == 0:
                print("Error: Division by zero!\n")
                continue
            result = num1 / num2

        print(f"Result: {result}\n")


if __name__ == "__main__":
    calculator()
