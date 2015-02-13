def rec_flatten(l, max_depth):
    if max_depth < 1:
        return l
    ret = []
    try:
        for item in l:
            flattened = rec_flatten(item, max_depth - 1)
            try:
                ret.extend(flattened)
            except TypeError:
                ret.append(flattened)
    except TypeError as err:
        # this very large try block relies on the for statement to be the only
        # thing that could raise a TypeError; if somehow some of the code
        # here were to raise a TypeError (because of a bug or something like that)
        # you'd silence the exception and raise an error
        return l
    return ret


def rec_flatten_without_exceptions(l, max_depth):
    # Your recursive flatten code, without using exceptions for flow control
    if not isinstance(l, (list, tuple)):
        return [l]  # always returns lists, so caller can extend
    if max_depth < 1:
        return l
    ret = []
    for item in l:
        flattened = rec_flatten_without_exceptions(item, max_depth - 1)
        ret.extend(flattened)
    return ret


def flatten(list_a, list_b, max_depth):
    # this mutates the lists, it's not wrong, and the exercise didn't specify
    # but it's un-Pythonic to mutate your fucntion's arguments
    list_a[:] = rec_flatten(list_a, max_depth)
    list_b[:] = rec_flatten(list_b, max_depth)


def flatten_after_feedback(list_a, list_b, max_depth):
    # Using suggested version
    return (rec_flatten_without_exceptions(list_a, max_depth),
            rec_flatten_without_exceptions(list_b, max_depth))


if __name__ == "__main__":
    # poor man's unittests..
    assert (
        rec_flatten_without_exceptions([(1, [2, 3]), [4, 'ana are mere']], 10) ==
        [1, 2, 3, 4, 'ana are mere'])
    assert (
        rec_flatten_without_exceptions([1, [2, 3], 4, 'ana are mere'], 1) ==
        [1, 2, 3, 4, 'ana are mere'])
    print "ok"
