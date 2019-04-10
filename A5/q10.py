"""
q10.py
"""


# Joshua Shin
# A01056181
# April 9th 2019


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


def database_shared_headings(outer_dictionary: dict) -> set:
    """
    Return the intersecting inner dictionary keys as a set.

    RETURN the intersecting inner dictionary keys as a set
    """
    return set.intersection(*[{key for key in inner_dictionary.keys()} for inner_dictionary in outer_dictionary.values()])


def main():
    print(database_shared_headings(dictionary))


if __name__ == "__main__":
    main()
