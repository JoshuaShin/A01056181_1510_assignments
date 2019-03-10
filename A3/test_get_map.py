from unittest import TestCase
from map import get_map


class TestGetMap(TestCase):
    def test_get_map(self):
        self.assertEqual(list("|                .     FEDERATION     *         .             |\n"), get_map()[10])

