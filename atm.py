balance = 5000

print("===== ATM MACHINE =====")
print("1. Check Balance")
print("2. Deposit")
print("3. Withdraw")
print("4. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Balance =", balance)

elif choice == 2:
    amount = int(input("Enter deposit amount: "))
    balance += amount
    print("Updated Balance =", balance)

elif choice == 3:
    amount = int(input("Enter withdraw amount: "))
    if amount <= balance:
        balance -= amount
        print("Updated Balance =", balance)
    else:
        print("Insufficient Balance")

elif choice == 4:
    print("Thank You!")

else:
    print("Invalid Choice")
