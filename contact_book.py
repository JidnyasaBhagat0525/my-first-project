expenses = []

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Delete Expense")
    print("5. Show Total Expense")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        name = input("Enter Expense Name: ")
        amount = float(input("Enter Amount: "))
        expenses.append([name, amount])
        print("Expense added successfully!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses found.")
        else:
            print("\nExpenses:")
            for i in range(len(expenses)):
                print(i + 1, ".", expenses[i][0], "- ₹", expenses[i][1])

    elif choice == "3":
        search = input("Enter Expense Name to search: ")
        found = False

        for expense in expenses:
            if expense[0].lower() == search.lower():
                print("Expense Found:")
                print("Name:", expense[0])
                print("Amount: ₹", expense[1])
                found = True
                break

        if not found:
            print("Expense not found.")

    elif choice == "4":
        if len(expenses) == 0:
            print("No expenses to delete.")
        else:
            for i in range(len(expenses)):
                print(i + 1, ".", expenses[i][0], "- ₹", expenses[i][1])

            delete = int(input("Enter expense number to delete: "))

            if 1 <= delete <= len(expenses):
                removed = expenses.pop(delete - 1)
                print(removed[0], "deleted successfully!")
            else:
                print("Invalid expense number.")

    elif choice == "5":
        total = 0
        for expense in expenses:
            total += expense[1]

        print("Total Expense: ₹", total)

    elif choice == "6":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.")
