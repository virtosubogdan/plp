import unittest

from plp.flatten import flatten_after_feedback as flatten


class TestFlatten(unittest.TestCase):
    def assertLists(self, list_a, list_a_expected, list_b, list_b_expected):
        self.assertEqual(list_a, list_a_expected,
                         'First list is not correct:' + str(list_a))
        self.assertEqual(list_b, list_b_expected,
                         'Second list is not correct:' + str(list_b))

    def test_nop(self):
        a = [1, 2]
        b = [3]
        (ra, rb) = flatten(a, b, 2)
        self.assertLists(ra, [1, 2], rb, [3])

    def test_simple(self):
        a = [1, 2, [1], [1, [2]]]
        b = [1, 2]
        (ra, rb) = flatten(a, b, 1)
        self.assertLists(ra, [1, 2, 1, 1, [2]], rb, [1, 2])

    def test_complicated(self):
        a = [0, [1, [2, [3, 4]]]]
        b = [[0, [1, [2, [3, 4]]]]]
        (ra, rb) = flatten(a, b, 3)
        self.assertLists(ra, [0, 1, 2, 3, 4], rb, [0, 1, 2, [3, 4]])

    def test_tuple(self):
        a = [0, [1, (2, [3, 4])]]
        b = [[0, [1, [2, (3, 4)]]]]
        (ra, rb) = flatten(a, b, 3)
        self.assertLists(ra, [0, 1, 2, 3, 4], rb, [0, 1, 2, (3, 4)])

    def test_no_flat(self):
        a = [[[1]]]
        b = []
        (ra, rb) = flatten(a, b, 1)
        self.assertLists(ra, [[1]], rb, [])


if __name__ == '__main__':
    unittest.main()
