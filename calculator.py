def add(a, b):
    return a + b

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
        elif choice in ("2", "3", "4"):
            print("This operation is not yet implemented.")
        else:
            print("Invalid input. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()