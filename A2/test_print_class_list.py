import io
from unittest.mock import patch
from unittest import TestCase
from dungeonsanddragons import print_class_list


class TestPrintClassList(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_class_list(self, mock_stdout):
        print_class_list()
        self.assertEqual("CLASS LIST:\nbarbarian\nbard\ncleric\ndruid\nfighter\nmonk\npaladin\n"
                         "ranger\nrogue\nsorcerer\nwarlock\nwizard\nblood hunter\n", mock_stdout.getvalue())
