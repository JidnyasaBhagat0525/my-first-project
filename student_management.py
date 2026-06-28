print("===== Student Management System =====")
print("1. Add Student")
print("2. Display Student")
print("3. Search Student")
print("4. Delete Student")
print("5. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
  name = input("Enter Student Name: ")
  print(name, "added successfully.")

elif choice == 2:
  print("Displaying student details...")
    
elif choice == 3:
  name = input("Enter Student Name to Search: ")
  print(name, "found.")

elif choice == 4:
  name = input("Enter Student Name to Delete: ")
  print(name, "Delete Successfully")

elif choice == 5:
    print("Thank You!")

else:
  print("Invalid Choice")
