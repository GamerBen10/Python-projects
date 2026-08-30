print("Welcome to the Daily Expense Tracker!\n")

expenseList = []

while True:
    print('\n ')
    print("\nMenu: \n ")
    print("1. Add a new expense")
    print("2. View all expenses")
    print("3. Calculate total and average expense")
    print("4. Clear all expenses")
    print("5. Exit")
    print('\n\n')
    choice = input(" \n Enter your choice (1-5): \n ")
    print('\n')
    if choice == "1":
        try:
            expense = float(input("Enter expense amount: "))
            expenseList.append(expense)
            print("Expense added successfully!")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    elif choice == "2":
        if not expenseList:
            print("No expenses recorded yet.")
        else:
            print("\nYour Expenses:")
            for index, expense in enumerate(expenseList, start=1):
                print(f"{index}. ${expense:.2f}")

    elif choice == "3":
        if not expenseList:
            print("No expenses recorded yet.")
        else:
            total = sum(expenseList)
            average = total / len(expenseList)
            print(f"Total Expenses: ${total:.2f}")
            print(f"Average Expense: ${average:.2f}")

    elif choice == "4":
        if not expenseList:
            print("No expenses recorded yet.")
        else:
            expenseList.clear()
            print("All expenses have been cleared!")

    elif choice == "5":
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break
        print("Invalid choice. Please enter a number betwee 1 - 5")
