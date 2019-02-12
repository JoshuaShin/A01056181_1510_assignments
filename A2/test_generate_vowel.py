from unittest import TestCase
from dungeonsanddragons import generate_vowel


class TestGenerateVowel(TestCase):
    def test_generate_vowel_length(self):
        self.assertEqual(len(generate_vowel()), 1)

    def test_generate_vowel_string(self):
        self.assertEqual(type(generate_vowel()), str)

    def test_generate_vowel_is_vowel(self):
        for i in range(1000):
            self.assertTrue(generate_vowel() in "aeiouy")
