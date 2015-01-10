import unittest

from plp.merge import merge


class TestMerge(unittest.TestCase):
    def test_plp(self):
        a = {'x': [1, 2, 3], 'y': 1, 'z': set([1, 2, 3]), 'w': 'qweqwe', 't': {'a': [1, 2]}, 'm': [1]}
        b = {'x': [4, 5, 6], 'y': 4, 'z': set([4, 2, 3]), 'w': 'asdf', 't': {'a': [3, 2]}, 'm': "wer"}
        c = merge(a, b)
        self.assertEqual(c, {'x': [1, 2, 3, 4, 5, 6], 'y': 5, 'z': set([1, 2, 3, 4]), 'w': 'qweqweasdf',
                             't': {'a': [1, 2, 3, 2]}, 'm': ([1], "wer")}, 'Result:' + str(c))

    def test_int(self):
        self.assertEqual(merge(1, 2), 3)

    def test_float(self):
        self.assertEqual(merge(1.4, 2.2), 3.6)

    def test_string(self):
        self.assertEqual(merge('1', '2'), '12')

    def test_set(self):
        self.assertEqual(merge({1, 2}, {2, 3}), {1, 2, 3})

    def test_lists(self):
        a = [1, 'a']
        b = [2, 'b']
        self.assertEqual(merge(a, b), [1, 'a', 2, 'b'])

    def test_illegal(self):
        with self.assertRaises(TypeError):
            merge((1, 2), (2, 3))