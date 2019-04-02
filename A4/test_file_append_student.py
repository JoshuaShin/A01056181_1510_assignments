from unittest import TestCase
import crud
import student


class TestFileAppendStudent(TestCase):
    def test_file_append_student(self):
        crud.file_append_student(student.Student("test", "test", "t12345678", True, []))
        self.assertTrue(crud.is_student_number_duplicate("t12345678"))
