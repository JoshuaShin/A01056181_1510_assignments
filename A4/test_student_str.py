from unittest import TestCase
from student import Student


class TestStudentStr(TestCase):
    def test___str___with_grades(self):
        student = Student("Test_first", "Test_last", "A12345678", True, [10.0, 10.0, 10.0])
        self.assertEqual("Test_First Test_Last A12345678 True 10.0 10.0 10.0", str(student))

    def test___str___no__grades(self):
        student = Student("Test_first", "Test_last", "A12345678", True, [])
        self.assertEqual("Test_First Test_Last A12345678 True ", str(student))
