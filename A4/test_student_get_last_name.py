from unittest import TestCase
from student import Student


class TestStudentGetLastName(TestCase):
    def test_get_last_name(self):
        student = Student("Test_First", "Test_Last", "A12345678", True, [10.0, 10.0, 10.0])
        self.assertEqual("Test_Last", student.get_last_name())
