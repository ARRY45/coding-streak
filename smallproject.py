students = []


def add_student():
    name = input("Enter student name: ")
    marks = []

    for i in range(5):
        mark = float(input(f"Enter marks for subject {i + 1}: "))
        marks.append(mark)

    students.append({
        "name": name,
        "marks": marks
    })

    print("Student added successfully!")


def calculate_result(student):
    total = sum(student["marks"])
    percentage = total / len(student["marks"])

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    return total, percentage, grade


def display_students():
    if len(students) == 0:
        print("No students found.")
        return

    for student in students:
        total, percentage, grade = calculate_result(student)

        print("\n-------------------------")
        print("Name       :", student["name"])
        print("Marks      :", student["marks"])
        print("Total      :", total)
        print("Percentage :", percentage)
        print("Grade      :", grade)


def search_student():
    name = input("Enter student name to search: ")

    for student in students:
        if student["name"].lower() == name.lower():
            total, percentage, grade = calculate_result(student)

            print("\nStudent Found!")
            print("Name       :", student["name"])
            print("Marks      :", student["marks"])
            print("Total      :", total)
            print("Percentage :", percentage)
            print("Grade      :", grade)
            return

    print("Student not found.")


while True:

    print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        print("Program ended.")
        break

    else:
        print("Invalid choice!")