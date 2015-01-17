from unittest import TestCase
from plp.singleton import SingletonClass


class Single(object):
    __metaclass__ = SingletonClass


class Single2(object):
    __metaclass__ = SingletonClass

    def __init__(self, a, b=3):
        self.a = a
        self.b = b


class TestSingleton(TestCase):
    def test_equal(self):
        self.assertTrue(Single() == Single())

    def test_param_class(self):
        a = Single2('a')
        b = Single2('b', b=5)
        self.assertEqual(a.b, b.b)
        self.assertTrue(a == b)
