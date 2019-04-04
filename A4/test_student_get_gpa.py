from unittest import TestCase
from student import Student


class TestStudentGetGpa(TestCase):
    def test_get_gpa(self):
        student = Student("Test_First", "Test_Last", "A12345678", True, [10.0, 20.0, 30.0])
        self.assertEqual(20.0, student.get_gpa())

    def test_get_gpa_no_grades(self):
        student = Student("Test_First", "Test_Last", "A12345678", True, [])
        self.assertEqual(None, student.get_gpa())
