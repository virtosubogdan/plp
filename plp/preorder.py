# -*- coding: utf-8 -*-
from Queue import LifoQueue
# the Queue module is for multithreading
# if you want a simple stack, you can append and pop on a list
# you really don't need the overhead of the locks
# according to the tests it's over 10 times slower


# awesome, this is very compact and very readable code
#  %timeit list(preorder.preorder_rec(('b', ('a', None, None), ('z', ('c', None, None), ('zz', None, None)))))
# 100000 loops, best of 3: 2.94 µs per loop
def preorder_rec(tree):
    if tree is None:
        return
    root, left, right = tree
    yield root
    for item in preorder_rec(left):  # i suspect you wanted to call the recursive version here
        yield item
    for item in preorder_rec(right):  # i suspect you wanted to call the recursive version here
        yield item


# In [14]: %timeit list(preorder.preorder(('b', ('a', None, None), ('z', ('c', None, None), ('zz', None, None)))))
# 10000 loops, best of 3: 40.5 µs per loop
def preorder(tree):
    if tree is None:
        return
    rest = LifoQueue()
    rest.put(tree)
    while not rest.empty():
        root, left, right = rest.get()
        if root is None:
            continue
        yield root
        if right is not None:
            rest.put(right)
        if left is not None:
            rest.put(left)


# same code as above, using list instead of LifoQueue
# In [15]: %timeit list(preorder.preorder_list(('b', ('a', None, None), ('z', ('c', None, None), ('zz', None, None)))))
# 100000 loops, best of 3: 2.96 µs per loop
def preorder_list(tree):
    if tree is None:
        return
    rest = []
    rest.append(tree)
    while not len(rest) == 0:
        root, left, right = rest.pop()
        if root is None:
            continue
        yield root
        if right is not None:
            rest.append(right)
        if left is not None:
            rest.append(left)


class PreOrderIterator(object):
    def __init__(self, tree):
        self.rest = []  # LifoQueue()
        self.rest.append(tree)

    def __iter__(self):
        return self

    def next(self):
        if len(self.rest) == 0:
            raise StopIteration
        root, left, right = self.pop.get()
        if root is None:
            raise StopIteration
        if right is not None:
            self.rest.append(right)
        if left is not None:
            self.rest.append(left)
        return root
