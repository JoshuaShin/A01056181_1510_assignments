import io
from unittest.mock import patch
from unittest import TestCase
import crud
import student


class TestFileRead(TestCase):
    def test_file_read_blank(self):
        crud.file_write([])
        self.assertEqual(0, len(crud.file_read()))

    def test_file_read(self):
        student_1 = student.Student("test", "test", "t11111111", "True", [])
        student_2 = student.Student("test", "test", "t22222222", "True", [])

        crud.file_write([student_1, student_2])
        students = crud.file_read()
        self.assertTrue(student_1.get_student_number() in students[0].get_student_number()
                        and student_2.get_student_number() in students[1].get_student_number())
        crud.file_write([])
