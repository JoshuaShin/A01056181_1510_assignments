from unittest import TestCase
from student import Student


class TestStudentSetFinalGrade(TestCase):
    def test_set_final_grades(self):
        student = Student("Test_First", "Test_Last", "A12345678", False, [])
        student.set_final_grades([10.0, 20.0, 30.0])
        self.assertEqual([10.0, 20.0, 30.0], student.get_final_grades())

    def test_set_final_grades_not_a_number(self):
        student = Student("Test_First", "Test_Last", "A12345678", False, [])
        with self.assertRaises(ValueError):
            student.set_final_grades(['not a number'])

    def test_set_final_grades_out_of_range_low(self):
        student = Student("Test_First", "Test_Last", "A12345678", False, [])
        with self.assertRaises(ValueError):
            student.set_final_grades([-0.01])

    def test_set_final_grades_out_of_range_high(self):
        student = Student("Test_First", "Test_Last", "A12345678", False, [])
        with self.assertRaises(ValueError):
            student.set_final_grades([100.01])
