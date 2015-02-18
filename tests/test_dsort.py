import unittest
import random
import string
from timeit import timeit

from plp.dsort import d_sort_improved as d_sort, q_sort, d_compare_sort, l_compare


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


def randomWord(size=3):
    word = ''
    for _ in range(size):
        word += random.choice(string.ascii_lowercase)
    return word


def generateInput(dict_size=1000, value_range=100):
    dicts = []
    lists = []
    for _ in range(2):
        dictionary = {}
        list_form = []
        for _ in range(random.randint(0, dict_size)):
            key = randomWord()
            if key in dictionary:
                continue
            value = random.randint(0, value_range)
            dictionary[key] = value
            list_form.append((key, value))
        dicts.append(dictionary)
        lists.append(list_form)
    return (dicts[0], dicts[1], lists[0], lists[1])

if __name__ == '__main__':
    # unittest.main()

    dict1, dict2, list1, list2 = generateInput()

    time_old = timeit("d_compare_sort(dict1, dict2)",
                      setup="from __main__ import d_compare_sort, dict1, dict2", number=1000)
    time_new = timeit("l_compare(list1, list2, True)",
                      setup="from __main__ import l_compare, list1, list2", number=1000)
    print "Time old: {}, time new: {}, speedup: {}".format(time_old, time_new, time_old/time_new)
