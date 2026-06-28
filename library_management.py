print("===== LIBRARY MANAGEMENT SYSTEM =====")
print("1. Issue Book")
print("2. Return Book")
print("3. Search Book")
print("4. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
    book = input("Enter Book Name: ")
    print(book, "issued successfully.")

elif choice == 2:
    book = input("Enter Book Name: ")
    print(book, "returned successfully.")

elif choice == 3:
    book = input("Enter Book Name: ")
    print(book, "is available in library.")

elif choice == 4:
    print("Thank You!")

else:
    print("Invalid Choice")
