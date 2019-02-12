from unittest import TestCase
from dungeonsanddragons import generate_syllable


class TestGenerateSyllable(TestCase):
    def test_generate_syllable_string(self):
        self.assertEqual(type(generate_syllable()), str)

    def test_generate_syllable_length(self):
        self.assertEqual(len(generate_syllable()), 2)

    def test_generate_syllable_consonant(self):
        for i in range(1000):
            self.assertTrue(generate_syllable()[0] in "bcdfghjklmnpqrstvwxyz")

    def test_generate_syllable_vowel(self):
        for i in range(1000):
            self.assertTrue(generate_syllable()[1] in "aeiouy")
