from core.student import Student

def menu():
    print("""Menu:
        1 - Add student
        2 - Update
        3 - Print all
        4 - Calculate Graduation date
        5 - Save""")

def add_student(student: Student):
    student.id = input("StudentID: > ")
    student.name = input("Name: > ")
    student.gender = input("Gender: > ")
    student.age = input("Age: > ")
    student.enroll_date = input("Enrollment date: > ")
    student.midterm = input("Midterm: > ")
    student.final = input("Final: > ")
    student.add()

    print("New student added successfully! \n")

def update_student(student: Student):
    id = input("StudendID: > ")
    data = student.getStudent(id)

    if len(data) == 0:
        print("This student not found !")
    else:
        print("""Info:
            StudentID: {}
            Name: {}
            Gender: {}
            Age: {}
            Enrollment date: {}
            Midterm: {}
            Final: {}
            GPA: {}""".format(
                data["StudentID"], 
                data["Name"], 
                data["Gender"], 
                data["Age"],
                data["Enrollment date"],
                data["Midterm"],
                data["Final"],
                data["GPA"]
            )
        )

        print("\nPlease enter updated information ! \n")

        student.name = input("Name: > ")
        student.gender = input("Gender: > ")
        student.age = input("Age: > ")
        student.enroll_date = input("Enrollment date: > ")
        student.midterm = input("Midterm: > ")
        student.final = input("Final: > ")
        student.update(id)

        print("\nStudent updated successfully! \n")

def graduation_date(student: Student):
    id = input("StudendID: > ")
    data = student.getStudent(id)

    if len(data) == 0:
        print("This student not found !")
    else:
        print("""Info:
            Name: {}""".format(data["Name"])
        )
        print("\nPlease enter study duration! \nExample: 3 12\n\n")
        args = input("Study duration: > ")
        calculate = student.calculate_grad_date(data["Enrollment date"], args)

        print("\nGraduation date: {}\n\n".format(calculate))