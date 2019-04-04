from unittest import TestCase
from student import Student


class TestStudentSetInGoodStanding(TestCase):
    def test_set_in_good_standing(self):
        student = Student("Test_last", "Test_last", "A12345678", False, [10.0, 10.0, 10.0])
        student.set_in_good_standing(True)
        self.assertEqual(True, student.is_in_good_standing())
