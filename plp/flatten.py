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
    except TypeError:
        return l
    return ret


def flatten(list_a, list_b, max_depth):
    list_a[:] = rec_flatten(list_a, max_depth)
    list_b[:] = rec_flatten(list_b, max_depth)
