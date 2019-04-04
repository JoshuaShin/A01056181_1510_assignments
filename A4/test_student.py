from unittest import TestCase
from student import Student


class TestStudent(TestCase):
    def test___init__(self):
        student = Student("Test_first", "Test_last", "A12345678", True, [10.0, 10.0, 10.0])
        self.assertEqual("Test_First Test_Last A12345678 True 10.0 10.0 10.0", str(student))

    def test___init__no__grades(self):
        student = Student("Test_first", "Test_last", "A12345678", True, [])
        self.assertEqual("Test_First Test_Last A12345678 True ", str(student))

    def test___init__no__first_name(self):
        with self.assertRaises(ValueError):
            Student("", "Test_last", "A12345678", True, [])

    def test___init__no__last_name(self):
        with self.assertRaises(ValueError):
            Student("Test_first", "", "A12345678", True, [])

    def test___init__no__bad_student_number(self):
        with self.assertRaises(ValueError):
            Student("Test_first", "", "bad_student_number", True, [])
