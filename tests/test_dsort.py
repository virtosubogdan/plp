import unittest

from plp.dsort import d_sort_improved as d_sort, q_sort


class TestDSort(unittest.TestCase):
    def test_no_file(self):
        with self.assertRaises(IOError):
            d_sort('inexistent', 'inexistent')

    def test_simple(self):
        out_file = 'res/dict.out'
        open(out_file, 'w').close()
        d_sort('res/dict.in', out_file)
        self.assert_file_order(out_file, [2, 1, 0, 3])

    def test_eq_items(self):
        out_file = 'res/dict.out'
        open(out_file, 'w').close()
        d_sort('res/dict_eq.in', out_file)
        self.assert_file_order(out_file, [3, 1, 0, 4, 2, 5])

    def test_sort(self):
        self.assertEqual(q_sort([1, 5, 0, 2, 2, -2, 2], 0, 5,
                                lambda a, b: a > b),
                         [-2, 0, 1, 2, 2, 5, 2])

    def assert_file_order(self, out_file, expected_order):
        file_order = []
        with open(out_file) as out_file:
            for line in out_file:
                file_order.append(int(line))
        self.assertEqual(file_order, expected_order)


if __name__ == '__main__':
    unittest.main()
