from unittest import TestCase
import crud
import student


class TestFileWrite(TestCase):
    def test_file_write_blank(self):
        crud.file_write([])
        self.assertEqual(0, len(crud.file_read()))

    def test_file_write(self):
        crud.file_write([])
        student_1 = student.Student("test", "test", "t11111111", True, [])
        student_2 = student.Student("test", "test", "t22222222", True, [])

        crud.file_write([student_1, student_2])
        self.assertTrue(crud.file_read()[0].get_student_number() == "T11111111" and
                        crud.file_read()[1].get_student_number() == "T22222222")
        crud.file_write([])
