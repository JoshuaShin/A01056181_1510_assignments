from unittest import TestCase
from student import Student


class TestStudentSetFirstName(TestCase):
    def test_set_first_name(self):
        student = Student("Test_first", "Test_last", "A12345678", True, [10.0, 10.0, 10.0])
        student.set_first_name("New_Name")
        self.assertEqual("New_Name", student.get_first_name())

    def test_set_first_name_invalid(self):
        student = Student("Test_first", "Test_last", "A12345678", True, [10.0, 10.0, 10.0])
        with self.assertRaises(ValueError):
            student.set_first_name(" ")

