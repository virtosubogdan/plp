from itertools import combinations


def subset_comb(base_set):
    yield base_set
    for size in range(1, len(base_set)):
        for combination in combinations(base_set, size):
            yield {item for item in combination}
    yield set([])


def subset(base_set):
    enumerated_set = [x for x in enumerate(base_set)]
    for i in range(2 ** len(base_set)):
        yield {item for index, item in enumerated_set if i & (2 ** index)}
