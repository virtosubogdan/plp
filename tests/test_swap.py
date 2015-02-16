import unittest

from plp.swap import swap, IllegalArgument


class Immutable:
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
                and self.x == other.x)

    def __hash__(self):
        return self.x

    def __repr__(self):
        return '{Immutable:' + str(self.x) + '}'


class TestSwap(unittest.TestCase):
    def test_simple(self):
        dictionary = {'a': 123, 'b': 456}
        swap(dictionary)
        self.assertEqual(dictionary, {123: 'a', 456: 'b'})

    def test_impossible(self):
        with self.assertRaises(IllegalArgument):
            swap({'a': (1, 2, [3])})

    def test_reverse(self):
        dictionary = {'a': 1, 1: 'a'}
        swap(dictionary)
        self.assertEqual(dictionary, {1: 'a', 'a': 1})

    def test_permutation(self):
        dictionary = {'a': 1, 1: 'b', 'b': 'a'}
        swap(dictionary)
        self.assertEqual(dictionary, {1: 'a', 'b': 1, 'a': 'b'})

    def test_custom(self):
        dictionary = {'a': Immutable(1), 1: 'b'}
        swap(dictionary)
        self.assertEqual(dictionary, {Immutable(1): 'a', 'b': 1})

    def test_duplicate_key(self):
        with self.assertRaises(IllegalArgument):
            swap({'a': Immutable(1), 1: Immutable(1)})

if __name__ == '__main__':
    unittest.main()
