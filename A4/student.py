class Student:
    """
    Student class.
    """

    def __init__(self, first_name: str, last_name: str, student_number: str):
        self.__first_name = None
        self.set_first_name(first_name)

        self.__last_name = None
        self.set_last_name(last_name)

        self.__student_number = None
        self.__set_student_number(student_number)

        self.__probation = False
        self.__final_grades = []

    def __str__(self):
        return "Student:" + str(self.__first_name) + " " + str(self.__last_name) \
               + " student number: " + str(self.__student_number) \
               + " probation: " + str(self.__probation) \
               + " grades: " + str(self.__final_grades)

    def set_first_name(self, first_name: str):
        if len(first_name.strip()) == 0:  # TODO: CHECK IS ALPHA?
            raise ValueError("name cannot be whitespace or blank")
        else:
            self.__first_name = first_name

    def get_first_name(self):
        return self.__first_name

    def set_last_name(self, last_name: str):
        if len(last_name.strip()) == 0:  # TODO: CHECK IS ALPHA?
            raise ValueError("name cannot be whitespace or blank")
        else:
            self.__last_name = last_name

    def get_last_name(self):
        return self.__last_name

    def __set_student_number(self, student_number):
        if len(student_number) != 9:
            raise ValueError("student number must be 9 digits")
        elif not student_number[0].isalpha():
            raise ValueError("student number must start with character")
        elif not student_number[1:9].isdigit():
            raise ValueError("student number must have 8 numbers following character")
        else:
            self.__student_number = student_number

    def get_student_number(self):
        return self.__student_number

    def set_status(self, probation: bool):
        self.__probation = probation

    def get_status(self):
        return self.__probation

    def add_final_grade(self, final_grade: float):
        self.__final_grades.append(final_grade)

    def get_final_grade(self):
        return self.__final_grades
