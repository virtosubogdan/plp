from Queue import LifoQueue


def preorder_rec(tree):
    if tree is None:
        return
    root, left, right = tree
    yield root
    for item in preorder(left):
        yield item
    for item in preorder(right):
        yield item


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


class PreOrderIterator(object):
    def __init__(self, tree):
        self.rest = LifoQueue()
        self.rest.put(tree)

    def __iter__(self):
        return self

    def next(self):
        if self.rest.empty():
            raise StopIteration
        root, left, right = self.rest.get()
        if root is None:
            raise StopIteration
        if right is not None:
            self.rest.put(right)
        if left is not None:
            self.rest.put(left)
        return root