from unittest import TestCase
from dungeonsanddragons import generate_syllable


class TestGenerateSyllable(TestCase):
    def test_generate_syllable_length(self):
        self.assertEqual(len(generate_syllable()), 2)

    def test_generate_syllable_string(self):
        self.assertEqual(type(generate_syllable()), str)

    def test_generate_syllable_is_syllable(self):
        for i in range(1000):
            syllable = generate_syllable()
            self.assertTrue(syllable[0] in "bcdfghjklmnpqrstvwxyz")
            self.assertTrue(syllable[1] in "aeiouy")
