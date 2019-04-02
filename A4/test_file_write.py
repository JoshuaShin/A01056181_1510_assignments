from unittest import TestCase
import crud
import student


class TestFileWrite(TestCase):
    def test_file_write_blank(self):
        crud.file_write([])
        self.assertEqual(0, len(crud.file_read()))

    def test_file_write(self):
        student_1 = student.Student("test", "test", "t11111111", True, [])
        student_2 = student.Student("test", "test", "t22222222", True, [])

        crud.file_write([student_1, student_2])
        self.assertTrue(crud.is_student_number_duplicate("t11111111") and crud.is_student_number_duplicate("t11111111"))
        crud.file_write([])
