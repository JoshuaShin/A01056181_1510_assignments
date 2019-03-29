"""
crud.py

Student Management System can be used to create, read, update and delete student data into student.txt
"""

# Joshua Shin
# A01056181
# Mar 1st 2019


def execute_command(user_input: int):
    if user_input == 1:
        pass
    elif user_input == 2:
        pass
    elif user_input == 3:
        pass
    elif user_input == 4:
        pass
    else:
        pass


def main():
    while True:
        try:
            user_input = int(input("1. Add student\n"
                                   "2. Delete student\n"
                                   "3. Calculate class average\n"
                                   "4. Print class list\n"
                                   "5. Quit\n"))
        except ValueError:
            print("Invalid command")
        else:
            execute_command(user_input)


if __name__ == "__main__":
    main()
