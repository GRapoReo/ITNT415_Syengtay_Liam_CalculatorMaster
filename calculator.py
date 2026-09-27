def add(a, b):
    """Return the sum of a and b."""
    # Handles both int and float inputs
    return a + b

def subtract(a, b):
    """Return the result of a minus b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

def main():
    while True:
        print("\n--- Calculator Menu ---")
        print("1. Add")
        print("2. Sub")
        print("3. Multi")
        print("4. Divi")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "5":
            print("Goodbye!")
            break
        elif choice == "1":
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print("Result:", add(a, b))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        elif choice == "2":
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print("Result:", subtract(a, b))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
            except Exception as e:
                print("An unexpected error occurred:", e)
        elif choice == "3":
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print("Result:", multiply(a, b))
            except ValueError:
                print("Invalid input. Please enter numeric values only.")
            except Exception as e:
                print("An unexpected error occurred:", e)
        elif choice == "4":
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                print("Result:", divide(a, b))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        else:
            print("Invalid input. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()