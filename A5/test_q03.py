from unittest import TestCase
from unittest.mock import patch
import q03
import io


class TestBackup(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_backup_invalid_file(self, mock_stdout):
        q03.backup("invalid.txt")
        self.assertTrue("File does not exist." in mock_stdout.getvalue())

    def test_backup_valid_file(self):
        with open("valid.txt", 'w') as file_object:
            contents = "test\ntest\ntest"
            file_object.write(contents)
        q03.backup("valid.txt")
        with open("valid.bak") as new_file:
            self.assertEqual(contents, new_file.read())
