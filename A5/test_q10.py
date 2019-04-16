from unittest import TestCase
import q10


class TestDatabaseSharedHeadings(TestCase):

    def test_database_shared_headings_invalid(self):
        with self.assertRaises(TypeError):
            q10.database_shared_headings({})

    def test_database_shared_headings_return_type(self):
        dictionary = {'jgoodall': {'surname': 'Goodall',
                                   'name': 'Jane',
                                   'born': 1934,
                                   'died': None,
                                   'notes': 'Primate research',
                                   'author': ['In the Shadow of Man', 'The Chimps of Gombe']},
                      'rfranklin': {'surname': 'Franklin',
                                    'name': 'Rosalind',
                                    'born': 1920,
                                    'died': 1957,
                                    'notes': 'DNA research'},
                      'aturing': {'surname': 'Turing',
                                  'name': 'Alan',
                                  'born': 1912,
                                  'died': 1954,
                                  'notes': 'polymath',
                                  'author': ['Systems of Logic based on Ordinals']}}
        self.assertEqual(set, type(q10.database_shared_headings(dictionary)))

    def test_database_shared_headings_valid(self):
        dictionary = {'jgoodall': {'surname': 'Goodall',
                                   'name': 'Jane',
                                   'born': 1934,
                                   'died': None,
                                   'notes': 'Primate research',
                                   'author': ['In the Shadow of Man', 'The Chimps of Gombe']},
                      'rfranklin': {'surname': 'Franklin',
                                    'name': 'Rosalind',
                                    'born': 1920,
                                    'died': 1957,
                                    'notes': 'DNA research'},
                      'aturing': {'surname': 'Turing',
                                  'name': 'Alan',
                                  'born': 1912,
                                  'died': 1954,
                                  'notes': 'polymath',
                                  'author': ['Systems of Logic based on Ordinals']}}
        self.assertEqual({'died', 'surname', 'notes', 'name', 'born'}, q10.database_shared_headings(dictionary))
