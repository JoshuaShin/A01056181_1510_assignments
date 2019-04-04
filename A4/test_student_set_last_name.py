from unittest import TestCase
from student import Student


class TestStudentSetLastName(TestCase):
    def test_set_last_name(self):
        student = Student("Test_last", "Test_last", "A12345678", True, [10.0, 10.0, 10.0])
        student.set_last_name("New_Name")
        self.assertEqual("New_Name", student.get_last_name())

    def test_set_last_name_invalid(self):
        student = Student("Test_last", "Test_last", "A12345678", True, [10.0, 10.0, 10.0])
        with self.assertRaises(ValueError):
            student.set_last_name(" ")

