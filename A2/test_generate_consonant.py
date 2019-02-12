from unittest import TestCase
from dungeonsanddragons import generate_consonant


class TestGenerateConsonant(TestCase):
    def test_generate_consonant_string(self):
        self.assertEqual(type(generate_consonant()), str)

    def test_generate_consonant_length(self):
        self.assertEqual(len(generate_consonant()), 1)

    def test_generate_consonant_is_consonant(self):
        for i in range(1000):
            self.assertTrue(generate_consonant() in "bcdfghjklmnpqrstvwxyz")
