from unittest import TestCase
from student import Student


class TestStudentAddFinalGrade(TestCase):
    def test_add_final_grade(self):
        student = Student("Test_First", "Test_Last", "A12345678", False, [])
        student.add_final_grade(10.0)
        self.assertEqual([10.0], student.get_final_grades())

    def test_add_final_grade_not_a_number(self):
        student = Student("Test_First", "Test_Last", "A12345678", False, [])
        with self.assertRaises(ValueError):
            student.add_final_grade('not a number')

    def test_add_final_grade_out_of_range_low(self):
        student = Student("Test_First", "Test_Last", "A12345678", False, [])
        with self.assertRaises(ValueError):
            student.add_final_grade(-0.01)

    def test_add_final_grade_out_of_range_high(self):
        student = Student("Test_First", "Test_Last", "A12345678", False, [])
        with self.assertRaises(ValueError):
            student.add_final_grade(100.01)
