from unittest import TestCase
import crud
import student


class TestFileAppendStudent(TestCase):
    def test_file_append_student(self):
        crud.file_write([])
        crud.file_append_student(student.Student("test", "test", "t12345678", True, []))
        self.assertEqual(crud.file_read()[0].get_student_number(), "T12345678")
        crud.file_write([])
