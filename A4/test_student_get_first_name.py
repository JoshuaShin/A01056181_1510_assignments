from unittest import TestCase
from student import Student


class TestStudentGetFirstName(TestCase):
    def test_get_first_name(self):
        student = Student("Test_First", "Test_Last", "A12345678", True, [10.0, 10.0, 10.0])
        self.assertEqual("Test_First", student.get_first_name())
