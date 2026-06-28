print("===== BANK MANAGEMENT SYSTEM =====")
print("1. Deposit")
print("2. Withdraw")
print("3. Check Balance")
print("4. Exit")

balance = 1000

choice = int(input("Enter your choice: "))

if choice == 1:
    amount = int(input("Enter Deposit Amount: "))
    balance = balance + amount
    print("Updated Balance =", balance)

elif choice == 2:
    amount = int(input("Enter Withdraw Amount: "))
    if amount <= balance:
        balance = balance - amount
        print("Updated Balance =", balance)
    else:
        print("Insufficient Balance")

elif choice == 3:
    print("Current Balance =", balance)

elif choice == 4:
    print("Thank You!")

else:
    print("Invalid Choice")
