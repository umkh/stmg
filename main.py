import os

from core.student import Student
import helper

file = os.path.abspath(os.getcwd())+"/core/database.txt"

if __name__ == "__main__":
    student = Student(file)

    print("------Welcome to Student Management------\n")
    choice = ""

    while choice.lower() != "x":
        helper.menu()

        choice = input("\nPlease select menu: > ")

        if choice == "1":
            helper.add_student(student)

        elif choice == "2":
            helper.update_student(student)

        elif choice == "3":
            student.printAll()
        
        elif choice == "4":
            helper.graduation_date(student)

        elif choice == "5":
            student.save_to_disk()
            print("Students saved successfully!")

        elif choice.lower() == "x":
            print("Thank you! Shutting down.")

        else:
            print("Sorry, I didnt recognise that option")
