class Student:
    """
    Student class.
    """

    def __init__(self, first_name: str, last_name: str, student_number: str, good_standing: str, grades: list):
        self.__first_name = None
        self.set_first_name(first_name)

        self.__last_name = None
        self.set_last_name(last_name)

        self.__student_number = None
        self.__set_student_number(student_number)

        self.__good_standing = None
        self.set_good_standing(good_standing)

        self.__final_grades = []
        self.set_final_grades(grades)

    def __str__(self):
        return ' '.join((self.__first_name,
                         self.__last_name,
                         self.__student_number,
                         str(self.__good_standing),
                         ' '.join(str(grade) for grade in self.__final_grades)))

    def set_first_name(self, first_name: str):
        if len(first_name.strip()) == 0:
            raise ValueError("name cannot be whitespace or blank")
        else:
            self.__first_name = first_name.title()

    def get_first_name(self):
        return self.__first_name

    def set_last_name(self, last_name: str):
        if len(last_name.strip()) == 0:
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

    def set_good_standing(self, good_standing: str):
        if good_standing.strip().title() == "True":
            self.__good_standing = True
        elif good_standing.strip().title() == "False":
            self.__good_standing = False
        else:
            raise ValueError("good standing must be 'True' or 'False'")

    def is_good_standing(self):
        return self.__good_standing

    def add_final_grade(self, final_grade):
        if not(type(final_grade) == float or type(final_grade) == int):
            raise ValueError("grade must a number")
        elif not 0 <= final_grade <= 100:
            raise ValueError("grade must be between 0 and 100")
        else:
            self.__final_grades.append(round(final_grade, 2))

    def set_final_grades(self, final_grades: list):
        for final_grade in final_grades:
            self.add_final_grade(final_grade)

    def get_final_grades(self):
        return self.__final_grades

    def get_gpa(self):
        if self.__final_grades:
            return sum(self.__final_grades) / len(self.__final_grades)
        else:
            return None
