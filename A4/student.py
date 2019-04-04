"""
student.py

Student class.
"""


# Joshua Shin
# A01056181
# Mar 31st 2019


class Student:
    """
    Student class

    Represent a student with first name, last name, student number, academic standing, and list of grades.
    """
    def __init__(self, first_name: str, last_name: str, student_number: str, in_good_standing: bool, grades: list):
        """
        Initialize student object

        POST-CONDITION Initialize student object
        """
        self.__first_name = None
        self.set_first_name(first_name)

        self.__last_name = None
        self.set_last_name(last_name)

        self.__student_number = None
        self.__set_student_number(student_number)

        self.__in_good_standing = None
        self.set_in_good_standing(in_good_standing)

        self.__final_grades = []
        self.set_final_grades(grades)

    def __str__(self) -> str:
        """
        Return a string representation of Student object.

        RETURN string representation of Student object
        """
        return ' '.join((self.__first_name,
                         self.__last_name,
                         self.__student_number,
                         str(self.__in_good_standing),
                         ' '.join(str(grade) for grade in self.__final_grades)))

    def set_first_name(self, first_name: str):
        """
        Set first name of Student object.

        POST-CONDITION ValueError is raised if first name is invalid
        POST-CONDITION first name is set if valid
        """
        if len(first_name.strip()) == 0:
            raise ValueError("name cannot be whitespace or blank")
        # if not first_name.strip().isalpha():
        #     raise ValueError("name must be composed of characters")
        else:
            self.__first_name = first_name.title()

    def get_first_name(self) -> str:
        """
        Return the first name of Student object.

        RETURN first name of Student object
        """
        return self.__first_name

    def set_last_name(self, last_name: str):
        """
        Set last name of Student object.

        POST-CONDITION ValueError is raised if last name is invalid
        POST-CONDITION last name is set if valid
        """
        if len(last_name.strip()) == 0:
            raise ValueError("name cannot be whitespace or blank")
        # if not last_name.strip().isalpha():
        #     raise ValueError("name must be composed of characters")
        else:
            self.__last_name = last_name.title()

    def get_last_name(self) -> str:
        """
        Return the last name of Student object.

        RETURN last name of Student object
        """
        return self.__last_name

    def __set_student_number(self, student_number: str):
        """
        Set student number of Student object.

        POST-CONDITION ValueError is raised if student number is invalid
        POST-CONDITION student number is set if valid
        """
        if len(student_number) != 9:
            raise ValueError("student number must be 9 digits")
        elif not student_number[0].isalpha():
            raise ValueError("student number must start with character")
        elif not student_number[1:9].isdigit():
            raise ValueError("student number must have 8 numbers following character")
        else:
            self.__student_number = student_number.title()

    def get_student_number(self) -> str:
        """
        Return the student number of Student object.

        RETURN student number of Student object
        """
        return self.__student_number

    def set_in_good_standing(self, in_good_standing: bool):
        """
        Set in good standing status of Student object.

        POST-CONDITION in good standing status is set
        """
        self.__in_good_standing = in_good_standing

    def is_in_good_standing(self) -> bool:
        """
        Return the academic standing of Student object.

        RETURN academic standing of Student object
        """
        return self.__in_good_standing

    def add_final_grade(self, final_grade):
        """
        Add a grade to final grades list of Student object.

        POST-CONDITION ValueError is raised if grade is invalid
        POST-CONDITION grade is added if valid
        """
        if not(type(final_grade) == float or type(final_grade) == int):
            raise ValueError("grade must a number")
        elif not 0 <= final_grade <= 100:
            raise ValueError("grade must be between 0 and 100")
        else:
            self.__final_grades.append(round(final_grade, 2))

    def set_final_grades(self, final_grades: list):
        """
        Set grades as final grades list of Student object.

        POST-CONDITION ValueError is raised if grades are invalid
        POST-CONDITION grades are set if valid
        """
        for final_grade in final_grades:
            self.add_final_grade(final_grade)

    def get_final_grades(self) -> list:
        """
        Return the grades of Student object.

        RETURN grades of Student object
        """
        return self.__final_grades

    def get_gpa(self):
        """
        Return the GPA of Student object.

        RETURN GPA of Student object
        RETURN None if student has no grades
        """
        if self.__final_grades:
            return sum(self.__final_grades) / len(self.__final_grades)
        else:
            return None
