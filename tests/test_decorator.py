import unittest
from time import sleep

from plp.decorator import time_slow


class TestDSort(unittest.TestCase):
    def test_instant(self):
        myfast()

    def test_slow(self):
        myslow()


@time_slow
def myfast():
    pass


@time_slow(threshold=0.05)
def myslow():
    sleep(0.5)
