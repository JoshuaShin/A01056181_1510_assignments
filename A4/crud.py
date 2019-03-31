"""
crud.py

Student Management System can be used to create, read, update and delete student data into student.txt
"""

# Joshua Shin
# A01056181
# Mar 1st 2019

from student import Student


def file_delete_student(student_number):
    deleted = False
    if len(student_number) == 9:
        with open("students.txt", "r+") as file_object:
            lines = file_object.readlines()
            file_object.truncate(0)
            for line in lines:
                if student_number + ' ' not in line:
                    file_object.write(line)
                else:
                    deleted = True
    return deleted


def file_append_student(new_student):
    with open("students.txt", "a") as file_object:
        file_object.write(str(new_student) + '\n')


def file_write(students):
    with open("students.txt", "w") as file_object:
        for student in students:
            file_object.write(str(student) + '\n')


def file_read():
    try:
        with open("students.txt") as file_object:
            student_list = []
            for line in file_object.readlines():
                student_list.append(string_to_student(line))
            return student_list
    except FileNotFoundError:
        return []


def string_to_student(line: str):
    student_info = line.split()
    first_name = student_info[0]
    last_name = student_info[1]
    student_number = student_info[2]
    if student_info[3] == "True":
        good_standing = True
    else:
        good_standing = False
    if len(student_info) == 4:
        grades = []
    else:
        grades = [float(grade) for grade in student_info[4:]]
    return Student(first_name, last_name, student_number, good_standing, grades)


def add_student():
    print("===== Add Student =====")
    first_name = input("Input first name: ")
    last_name = input("Input last name: ")
    student_number = input("Input student number: ")
    good_standing = "False"  # input("Input good_standing status: ")
    grades = "1 2 3 4 5"   # TODO: UNFINISHED

    try:
        student_instance = string_to_student(' '.join((first_name, last_name, student_number, good_standing, grades)))
    except ValueError as e:
        print("ERROR:", e)
    else:
        file_append_student(student_instance)
        # print(student_instance)
        print("Student added successfully")


def add_grade():
    print("===== Add grade =====")
    student_number = input("Student number: ").strip().title()
    students = file_read()
    for student in students:
        if student.get_student_number() == student_number:
            grade = input("Grade: ")
            try:
                student.add_final_grade(float(grade))
            except ValueError:
                print("Invalid grade")
                return
            file_write(students)
            print("Grade added successfully")
            return
    print(student_number, "does not exist")


def delete_student():
    print("===== Delete Student =====")
    student_number = input("Student number: ").strip().title()
    deleted = file_delete_student(student_number)

    if deleted:
        print(student_number, "deleted from database")
    else:
        print(student_number, "does not exist")


def calculate_class_average():
    print("===== Calculate Class Average =====")
    students = file_read()
    total_grades = 0
    total_students = 0
    for student in students:
        if student.get_gpa() is not None:
            total_grades += student.get_gpa()
            total_students += 1
    try:
        print("Class average:", total_grades / total_students)
    except ZeroDivisionError:
        print("Database is empty")


def print_class_list():
    print("===== Print Class List =====")
    print(*file_read(), sep='\n')


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
        add_grade()
    elif user_input == 3:
        delete_student()
    elif user_input == 4:
        calculate_class_average()
    elif user_input == 5:
        print_class_list()
    elif user_input == 6:
        quit_program()
    else:
        raise ValueError


def main():
    while True:
        try:
            execute_command(int(input("===== Enter Command =====\n"
                                      "1. Add student\n"
                                      "2. Add grade\n"
                                      "3. Delete student\n"
                                      "4. Calculate class average\n"
                                      "5. Print class list\n"
                                      "6. Quit\n"
                                      ">>> ")))
        except ValueError:
            print("Invalid command")


if __name__ == "__main__":
    main()
