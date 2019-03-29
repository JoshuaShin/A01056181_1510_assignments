"""
crud.py

Student Management System can be used to create, read, update and delete student data into student.txt
"""

# Joshua Shin
# A01056181
# Mar 1st 2019

import student


def file_write(new_student):
    with open("students.txt", "a") as file_object:
        file_object.write(new_student)


def file_read():
    try:
        with open("students.txt") as file_object:
            student_list = []
            for line in file_object.readlines():
                student_list.append(line_to_student(line))
            return student_list
    except FileNotFoundError:
        return []


def line_to_student(line: str):
    student_info = line.split()
    first_name = student_info[0]
    last_name = student_info[1]
    student_number = student_info[2]
    if student_info[3] == "True":
        probation = True
    else:
        probation = False
    if len(student_info) == 4:
        grades = []
    else:
        grades = student_info[4:]
    return student.Student(first_name, last_name, student_number, probation, grades)


def add_student():
    print("===== Add Student =====")
    first_name = input("Input first name: ")
    last_name = input("Input last name: ")
    student_number = input("Input student number: ")

    try:
        student_instance = student.Student(first_name, last_name, student_number)
    except ValueError as e:
        print("ERROR:", e)
    else:
        # TODO: WRITE STUDENT_INSTANCE TO FILE
        print("Student successfully added")
        print(student_instance)


def delete_student():
    print("===== Delete Student =====")


def calculate_class_average():
    print("===== Calculate Class Average =====")


def print_class_list():
    print("===== Print Class List =====")


def quit_program():
    """
    Quit program.

    POST-CONDITION program terminates
    """

    print("===== Program Terminated =====")
    quit()


def execute_command(user_input: int):
    if user_input == 1:
        add_student()
    elif user_input == 2:
        delete_student()
    elif user_input == 3:
        calculate_class_average()
    elif user_input == 4:
        print_class_list()
    else:
        quit_program()


def main():
    while True:
        try:
            user_input = int(input("===== Enter Command =====\n"
                                   "1. Add student\n"
                                   "2. Delete student\n"
                                   "3. Calculate class average\n"
                                   "4. Print class list\n"
                                   "5. Quit\n"
                                   ">>> "))
        except ValueError:
            print("Invalid command")
        else:
            execute_command(user_input)


if __name__ == "__main__":
    main()
