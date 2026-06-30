students = {}

while True:
    print("\n===== STUDENT RESULT MANAGEMENT =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Show Average Marks")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        name = input("Enter Student Name: ")
        marks = float(input("Enter Marks: "))

        if marks >= 90:
            grade = "A+"
        elif marks >= 80:
            grade = "A"
        elif marks >= 70:
            grade = "B"
        elif marks >= 60:
            grade = "C"
        elif marks >= 50:
            grade = "D"
        else:
            grade = "F"

        students[name] = [marks, grade]
        print("Student added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No student records found.")
        else:
            print("\nStudent Records:")
            for name, data in students.items():
                print("----------------------------")
                print("Name :", name)
                print("Marks:", data[0])
                print("Grade:", data[1])

    elif choice == "3":
        name = input("Enter Student Name to search: ")

        if name in students:
            print("Name :", name)
            print("Marks:", students[name][0])
            print("Grade:", students[name][1])
        else:
            print("Student not found.")

    elif choice == "4":
        name = input("Enter Student Name to update: ")

        if name in students:
            marks = float(input("Enter New Marks: "))

            if marks >= 90:
                grade = "A+"
            elif marks >= 80:
                grade = "A"
            elif marks >= 70:
                grade = "B"
            elif marks >= 60:
                grade = "C"
            elif marks >= 50:
                grade = "D"
            else:
                grade = "F"

            students[name] = [marks, grade]
            print("Marks updated successfully!")
        else:
            print("Student not found.")

    elif choice == "5":
        name = input("Enter Student Name to delete: ")

        if name in students:
            del students[name]
            print("Student deleted successfully!")
        else:
            print("Student not found.")

    elif choice == "6":
        if len(students) == 0:
            print("No student records available.")
        else:
            total = 0
            for data in students.values():
                total += data[0]

            average = total / len(students)
            print("Average Marks:", average)

    elif choice == "7":
        print("Thank you for using Student Result Management System!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 7.")
