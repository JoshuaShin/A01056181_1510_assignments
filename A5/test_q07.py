from unittest import TestCase
import q07


class TestPasswordValidator(TestCase):
    def test_password_validator_valid(self):
        self.assertTrue(q07.password_validator("helloThere3"))

    def test_password_validator_invalid_length(self):
        self.assertFalse(q07.password_validator("short"))

    def test_password_validator_invalid_no_lowercase(self):
        self.assertFalse(q07.password_validator("HELL0THERE"))

    def test_password_validator_invalid_no_uppercase(self):
        self.assertFalse(q07.password_validator("hell0there"))

    def test_password_validator_invalid_no_digit(self):
        self.assertFalse(q07.password_validator("helloThere"))
