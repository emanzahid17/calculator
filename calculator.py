def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 / num2

def exponentiation(num1, num2):
    return num1 ** num2

while True:
    print("\nSelect an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice (1-6): "))

        if choice == 6:
            print("Thank you for using the calculator! ")
            break

        if choice in [1, 2, 3, 4, 5]:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == 1:
                print("Result:", addition(num1, num2))
            elif choice == 2:
                print("Result:", subtraction(num1, num2))
            elif choice == 3:
                print("Result:", multiplication(num1, num2))
            elif choice == 4:
                print("Result:", division(num1, num2))
            elif choice == 5:
                print("Result:", exponentiation(num1, num2))
        else:
            print("Invalid choice. Please select a number between 1 and 6.")
            continue

    except ValueError:
        print("Invalid input. Please enter numbers only.")
        continue

    # Asking user if they want to continue or exit with validation
    while True:
        again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if again in ["yes", "y"]:
            break
        elif again in ["no", "n"]:
            print("Goodbye! 👋")
            exit()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")