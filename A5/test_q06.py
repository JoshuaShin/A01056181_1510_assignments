from unittest import TestCase
from unittest.mock import patch
import q06


class TestWebsite(TestCase):
    @patch('builtins.input', side_effect=["31edf4ft14rfa", "q4f1e12e4ta4a3"])
    def test_website_input_written(self, mock_input):
        q06.website()
        with open("index.html") as file_object:
            content = file_object.read()
        self.assertTrue("31edf4ft14rfa" in content and "q4f1e12e4ta4a3" in content)
