import collections


class IllegalArgument(Exception):
    pass


def has_hope(candidate):
    if not isinstance(candidate, collections.Hashable):
        return False
    if isinstance(candidate, collections.Iterable):
        for item in candidate:
            if item is not candidate and not has_hope(item):
                return False
    return True


def swap(dictionary):
    temp = {}
    for key, value in dictionary.items():
        if not has_hope(value):
            raise IllegalArgument('Swap is not possible: not hashable')
        if value in temp:
            raise IllegalArgument('Swap is not possible: duplicate key')
        temp[value] = key
        del dictionary[key]
    for key, value in temp.iteritems():
        dictionary[key] = value
