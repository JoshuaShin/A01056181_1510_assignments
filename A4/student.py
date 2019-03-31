class Student:
    """
    Student class.
    """

    def __init__(self, first_name: str, last_name: str, student_number: str, probation: bool, grades: list):
        self.__first_name = None
        self.set_first_name(first_name)

        self.__last_name = None
        self.set_last_name(last_name)

        self.__student_number = None
        self.__set_student_number(student_number)

        self.__probation = None
        self.set_probation_status(probation)

        self.__final_grades = []
        self.set_final_grade(grades)

    def __str__(self):
        return ' '.join((self.__first_name,
                         self.__last_name,
                         self.__student_number,
                         str(self.__probation),
                         ' '.join(str(grade) for grade in self.__final_grades)))

    def set_first_name(self, first_name: str):
        if len(first_name.strip()) == 0:  # TODO: CHECK IS ALPHA?
            raise ValueError("name cannot be whitespace or blank")
        else:
            self.__first_name = first_name.title()

    def get_first_name(self):
        return self.__first_name

    def set_last_name(self, last_name: str):
        if len(last_name.strip()) == 0:  # TODO: CHECK IS ALPHA?
            raise ValueError("name cannot be whitespace or blank")
        else:
            self.__last_name = last_name.title()

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
            self.__student_number = student_number.title()

    def get_student_number(self):
        return self.__student_number

    def set_probation_status(self, probation: bool):
        self.__probation = probation

    def get_probation_status(self):
        return self.__probation

    def add_final_grade(self, final_grade):
        if not(type(final_grade) == float or type(final_grade) == int):
            raise ValueError("grade must a number")
        elif not 0 <= final_grade <= 100:
            raise ValueError("grade must be between 0 and 100")
        else:
            self.__final_grades.append(round(final_grade, 2))

    def set_final_grade(self, final_grades: list):
        for final_grade in final_grades:
            self.add_final_grade(final_grade)

    def get_final_grade(self):
        return self.__final_grades
