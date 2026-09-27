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
            print("bye!")
            break
        elif choice in ("1", "2", "3", "4"):
            print("This operation is not yet implemented.")
        else:
            print("Invalid input. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()