from unittest import TestCase
from dungeonsanddragons import generate_name


class TestGenerateName(TestCase):
    def test_generate_name_string(self):
        self.assertEqual(type(generate_name(1)), str)

    def test_generate_name_length_short(self):
        self.assertEqual(len(generate_name(1)), 2)

    def test_generate_name_length_long(self):
        self.assertEqual(len(generate_name(100)), 200)

    def test_generate_name_capitalized(self):
        self.assertTrue(generate_name(1)[0].isupper())

    def test_generate_name_vowel(self):
        name = generate_name(100)
        for i in range(len(name)):
            if i % 2 == 1:
                self.assertTrue(name[i] in "aeiouy")

    def test_generate_name_consonant(self):
        name = generate_name(100).lower()
        for i in range(len(name)):
            if i % 2 == 0:
                self.assertTrue(name[i] in "bcdfghjklmnpqrstvwxyz")
