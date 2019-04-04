from unittest import TestCase
from student import Student


class TestStudentIsInGoodStanding(TestCase):
    def test_is_in_good_standing(self):
        student = Student("Test_First", "Test_Last", "A12345678", False, [10.0, 10.0, 10.0])
        self.assertEqual(False, student.is_in_good_standing())
