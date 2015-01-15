import unittest

from plp.preorder import preorder


class TestPreOrder(unittest.TestCase):
    def test_simple(self):
        tree = ('b', ('a', None, None), ('z', ('c', None, None), ('zz', None, None)))
        self.assertEqual([x for x in preorder(tree)], ['b', 'a', 'z', 'c', 'zz'])

    def test_order(self):
        tree = ('b', ('a', None, (1, None, (2, None, None))), ('z', ('c', None, None), ('zz', None, None)))
        self.assertEqual([x for x in preorder(tree)], ['b', 'a', 1, 2, 'z', 'c', 'zz'])