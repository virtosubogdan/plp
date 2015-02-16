def merge(a, b):
    if type(a) is not type(b):
        return a, b
    if (isinstance(a, int) or isinstance(b, float) or
            isinstance(a, str) or isinstance(a, list)):
        return a + b
    if isinstance(a, set):
        return a.union(b)
    # if isinstance(a, list):
    # return [merge(item1, item2) for item1, item2 in zip(a, b)]
    if isinstance(a, dict):
        return {key: merge(a[key], b[key]) for
                key in set(a.keys()).intersection(set(b.keys()))}
    raise TypeError('Unhandled types ' + str(type(a)) + ' and ' + str(type(b)))
