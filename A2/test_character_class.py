from unittest import TestCase
from dungeonsanddragons import character_class


class TestCharacterClass(TestCase):
    def test_character_class(self):
        class_list = {"barbarian": 12, "bard": 8, "cleric": 8, "druid": 8, "fighter": 10, "monk": 8, "paladin": 10,
                      "ranger": 10, "rogue": 8, "sorcerer": 6, "warlock": 8, "wizard": 6, "blood hunter": 10}
        self.assertEqual(class_list, character_class())
