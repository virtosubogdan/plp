import unittest

from plp.preorder import preorder, PreOrderIterator


class TestPreOrder(unittest.TestCase):
    def test_simple(self):
        tree = ('b', ('a', None, None), ('z', ('c', None, None), ('zz', None, None)))
        self.assertEqual([x for x in preorder(tree)], ['b', 'a', 'z', 'c', 'zz'])

    def test_order(self):
        tree = ('b', ('a', None, (1, None, (2, None, None))), ('z', ('c', None, None), ('zz', None, None)))
        self.assertEqual([x for x in preorder(tree)], ['b', 'a', 1, 2, 'z', 'c', 'zz'])

    def test_simple_iterator(self):
        tree = ('b', ('a', None, None), ('z', ('c', None, None), ('zz', None, None)))
        self.assertEqual([x for x in PreOrderIterator(tree)], ['b', 'a', 'z', 'c', 'zz'])

    def test_order_iterator(self):
        tree = ('b', ('a', None, (1, None, (2, None, None))), ('z', ('c', None, None), ('zz', None, None)))
        self.assertEqual([x for x in PreOrderIterator(tree)], ['b', 'a', 1, 2, 'z', 'c', 'zz'])