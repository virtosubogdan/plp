from unittest import TestCase
from plp.subset import subset


class TestSubset(TestCase):
    def test_simple(self):
        base_set = {1, 2, 3}
        result = [x for x in subset(base_set)]
        expected = [base_set, {2, 3}, {1, 3}, {3}, {1, 2}, {2}, {1}, set([])]
        self.assertItemsEqual(result, expected)

    def test_basic(self):
        base_set = {1, 'a'}
        result = [x for x in subset(base_set)]
        expected = [base_set, {1}, {'a'}, set([])]
        self.assertItemsEqual(result, expected)
