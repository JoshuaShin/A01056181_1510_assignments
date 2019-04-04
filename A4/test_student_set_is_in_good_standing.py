from unittest import TestCase
from student import Student


class TestStudentSetIsInGoodStanding(TestCase):
    def test_set_is_in_good_standing(self):
        student = Student("Test_last", "Test_last", "A12345678", True, [10.0, 10.0, 10.0])
        self.assertEqual(True, student.is_in_good_standing())
