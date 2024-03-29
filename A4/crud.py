"""
crud.py

Student Management System can be used to create, read, update and delete student data into students.txt.
"""


# Joshua Shin
# A01056181
# Mar 31st 2019


import doctest
from student import Student


def file_append_student(student: Student):
    """
    Add Student object to students.txt in string representation.

    POST-CONDITION Student object is added to students.txt
    """
    with open("students.txt", "a") as file_object:
        file_object.write(str(student) + '\n')


def file_write(students: list):
    """
    Add list of Student objects to students.txt in string representations.

    POST-CONDITION Student objects are added to students.txt
    """
    with open("students.txt", "w") as file_object:
        for student in students:
            file_object.write(str(student) + '\n')


def file_read() -> list:
    """
    Read and return Student objects saved in students.txt.

    RETURN list of Student objects saved in students.txt
    """
    try:
        with open("students.txt") as file_object:
            student_list = []
            for line in file_object.readlines():
                student_list.append(string_to_student(line))
            return student_list
    except FileNotFoundError:
        return []


def string_to_good_standing(standing: str) -> bool:
    """
    Translate strings true or false into boolean.

    POST-CONDITION ValueError is raised if standing is not 'True' or 'False'
    RETURN translated boolean

    >>> string_to_good_standing("True")
    True
    >>> string_to_good_standing("False")
    False
    """
    if standing.strip().title() == "True":
        return True
    elif standing.strip().title() == "False":
        return False
    else:
        raise ValueError("good standing must be 'True' or 'False'")


def string_to_student(line: str) -> Student:
    """
    Translate string representation of Student into Student object.

    PRE-CONDITION line representing Student object must be in valid format
    RETURN translated Student object
    """
    student_info = line.split()
    first_name = student_info[0]
    last_name = student_info[1]
    student_number = student_info[2]
    in_good_standing = string_to_good_standing(student_info[3])
    if len(student_info) == 4:
        grades = []
    else:
        grades = [float(grade) for grade in student_info[4:]]
    return Student(first_name, last_name, student_number, in_good_standing, grades)


def create_student() -> Student:
    """
    Aggregate user input to construct Student object.

    POST-CONDITION ValueError is raised if user input is invalid
    RETURN Student object of user input
    """
    first_name = input("Input first name (eg. Joshua): ").strip()
    last_name = input("Input last name (eg. Shin): ").strip()
    student_number = input("Input student number (eg. A12345678): ").strip().title()
    for student in file_read():
        if student.get_student_number() == student_number:
            raise ValueError("student number already exist")
    good_standing = string_to_good_standing(input("Input good standing status (eg. True or False): ").title())
    grades = input("Input grades separated by a space (eg. 70 80 90): ")
    try:
        grades = [float(grade) for grade in grades.split()]
    except ValueError:
        raise ValueError("invalid grades")
    return Student(first_name, last_name, student_number, good_standing, grades)


def add_student():
    """
    Add a string representation of Student object to student.txt according to user input.

    POST-CONDITION ValueError is raised if given information is invalid
    POST-CONDITION string representation of Student object is added to student.txt if valid
    """
    print("===== Add Student =====")
    try:
        student_instance = create_student()
    except ValueError as e:
        print("ERROR:", e)
    else:
        file_append_student(student_instance)
        print("Student added successfully")


def add_grade():
    """
    Add a grade onto the string representation of Student object in student.txt according to user input.

    POST-CONDITION ValueError is raised if user input is invalid
    POST-CONDITION grade is added onto the string representation of Student object in student.txt
    """
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
    """
    Delete the string representation of Student object from student.txt according to user input.

    POST-CONDITION string representation of Student object is deleted from student.txt if valid
    """
    print("===== Delete Student =====")
    student_number = input("Student number: ").strip().title()
    students = file_read()
    for student in students:
        if student.get_student_number() == student_number:
            students.remove(student)
            file_write(students)
            print(student_number, "deleted from database")
            return
    print(student_number, "does not exist")


def calculate_class_average():
    """
    Calculate the class average of the Student objects stored in student.txt.

    POST-CONDITION class average is printed if database is not empty
    """
    print("===== Calculate Class Average =====")
    students = file_read()
    total_grades = 0
    total_students = 0
    for student in students:
        if student.get_gpa() is not None:
            total_grades += student.get_gpa()
            total_students += 1
    try:
        print("Class average:", round(total_grades / total_students, 2))
    except ZeroDivisionError:
        print("No available grades")


def print_class_list():
    """
    Print the Student objects stored in student.txt.

    POST-CONDITION the Student objects stored in student.txt are printed
    """
    print("===== Print Class List =====")
    students = file_read()
    if students:
        print("FIRST NAME          LAST NAME           STUDENT NUMBER      GOOD STANDING       GRADES")
        for student in students:
            student_info = str(student).split()
            print(student_info[0], end=' ' * (20 - len(student_info[0])))
            print(student_info[1], end=' ' * (20 - len(student_info[1])))
            print(student_info[2], end=' ' * (20 - len(student_info[2])))
            print(student_info[3], end=' ' * (20 - len(student_info[3])))
            print(' / '.join(str(grade) for grade in student_info[4:]))
    else:
        print("Database is empty")


def quit_program():
    """
    Quit program.

    POST-CONDITION program terminates
    """
    print("===== Program Terminated =====")
    quit()


def execute_command(user_input: int):
    """
    Execute given user input.

    POST-CONDITION ValueError is raised if user input is invalid
    POST-CONDITION action corresponding user input is executed if valid
    """
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
    """
    Execute program loop.
    """
    doctest.testmod()
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
