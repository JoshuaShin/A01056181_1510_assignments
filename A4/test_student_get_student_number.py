from unittest import TestCase
from student import Student


class TestStudentGetStudentNumber(TestCase):
    def test_get_student_number(self):
        student = Student("Test_First", "Test_Last", "A12345678", True, [10.0, 10.0, 10.0])
        self.assertEqual("A12345678", student.get_student_number())
