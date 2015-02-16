__attr_er_message = 'Value %s does not have correct'\
                    '<key><whitespace><value> format'


def read_dicts(filename):
    with open(filename) as in_file:
        dicts = []
        current_dict = {}
        for line in in_file:
            if line.isspace():
                dicts.append(current_dict)
                current_dict = {}
            else:
                try:
                    a, b = line.split(' ')
                except ValueError:
                    raise AttributeError(__attr_er_message % line)
                current_dict[a] = int(b)
        if current_dict is not {}:
            dicts.append(current_dict)
        return dicts


def d_compare(dict1, dict2):
    for key1, key2 in zip(sorted(dict1.keys()), sorted(dict2.keys())):
        val1 = dict1[key1]
        val2 = dict2[key2]
        if val1 == val2:
            continue
        return val1 > val2


def q_sort(l, lo, hi, comparator):
    if lo >= hi:
        return l
    pivot, index = l[hi], lo
    for i, val in enumerate(l[lo:hi]):
        if comparator(pivot, val):
            l[lo + i], l[index], index = l[index], l[lo + i], index + 1
    l[index], l[hi] = l[hi], l[index]
    q_sort(l, lo, index - 1, comparator)
    q_sort(l, index + 1, hi, comparator)
    return l


def d_sort(in_filename, out_filename):
    dicts = read_dicts(in_filename)
    ordered_dicts = q_sort(dicts[:], 0, len(dicts) - 1, d_compare)
    count_appearances = {}
    with open(out_filename, 'w') as outFile:
        for item_order in [ordered_dicts.index(x) for x in dicts]:
            if item_order in count_appearances:
                outFile.write(str(item_order +
                                  count_appearances[item_order]) + '\n')
                count_appearances[item_order] += 1
            else:
                outFile.write(str(item_order) + '\n')
                count_appearances[item_order] = 1
