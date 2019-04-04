from unittest import TestCase
from student import Student


class TestStudentGetFinalGrades(TestCase):
    def test_get_final_grades(self):
        student = Student("Test_First", "Test_Last", "A12345678", True, [10.0, 10.0, 10.0])
        self.assertEqual([10.0, 10.0, 10.0], student.get_final_grades())
