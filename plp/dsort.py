__attr_er_message = 'Value %s does not have correct'\
                    '<key><whitespace><value> format'

# the speedup suggestions should be taken with a grain of salt
# they're technically correct, but they don't address the root cause of the slowness
# that's left as an exercise to the reader
# hint: the exercise talks about the input and output being dictionaries,
# but doesn't require you use dictionaries to implement


from itertools import izip


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


# %timeit dsort.d_compare(d1, d2)
# 10000 loops, best of 3: 156 us per loop
def d_compare(dict1, dict2):
    for key1, key2 in zip(sorted(dict1.keys()), sorted(dict2.keys())):
        val1 = dict1[key1]
        val2 = dict2[key2]
        if val1 == val2:
            continue
        return val1 > val2


# %timeit dsort.d_compare_izip(d1, d2)
# 10000 loops, best of 3: 139 us per loop
# if we use izip instead of zip, we don't need to build the whole list
# in memory up front, this has modest improvements
def d_compare_izip(dict1, dict2):
    for key1, key2 in izip(sorted(dict1.keys()), sorted(dict2.keys())):
        val1 = dict1[key1]
        val2 = dict2[key2]
        if val1 == val2:
            continue
        return val1 > val2


# %timeit dsort.d_compare_sort(d1, d2)
# 10000 loops, best of 3: 129 us per loop
# since keys returns a list that's safe to mutate,
# we can sort in place, instead of calling sorted to get a new list
def d_compare_sort(dict1, dict2):
    keys1, keys2 = dict1.keys(), dict2.keys()
    keys1.sort()
    keys2.sort()
    for key1, key2 in izip(keys1, keys2):
        val1 = dict1[key1]
        val2 = dict2[key2]
        if val1 == val2:
            continue
        return val1 > val2


# %timeit dsort.d_compare_items(d1, d2)
# 1000 loops, best of 3: 284 us per loop
# what if we eliminate the dictionary lookup?
# let's call items to get a list of tuples, and sort that
# nope, this is a major slowdown; probably from the overhead of allocating
# a lot more new objects
def d_compare_items(dict1, dict2):
    items1, items2 = dict1.items(), dict2.items()
    items1.sort()
    items2.sort()
    for (key1, val1), (key2, val2) in izip(items1, items2):
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

#%timeit d_sort('res/dict_eq.in','res/dict.out')
# 1000 loops, best of 3: 201 us per loop
# 10000 loops, best of 3: 190 us per loop
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

# Read the dictionaries in the file as lists with (key, value) items
# already ordered by key
def read_as_lists(filename):
    with open(filename) as in_file:
        lists = []
        current_list = []
        for line in in_file:
            if line.isspace():
                current_list.sort()
                lists.append(current_list)
                current_list = []
            else:
                try:
                    a, b = line.split(' ')
                except ValueError:
                    raise AttributeError(__attr_er_message % line)
                current_list.append((a, int(b)))
        if current_list != []:
            lists.append(current_list)
        return lists

# lists have (key,value) pairs and are ordered by key
def l_compare(list1, list2):
    for (key1, val1), (key2, val2) in izip(list1, list2):
        if val1 == val2:
            continue
        return val1 > val2

# Tried to improve by using lists with (key,value) items instead of dictionaries
# so the ordering of the elements can be used.
# %timeit d_sort_improved('res/dict_eq.in','res/dict.out')
# 10000 loops, best of 3: 196 us per loop
def d_sort_improved(in_filename, out_filename):
    lists = read_as_lists(in_filename)
    ordered_lists = q_sort(lists[:], 0, len(lists) - 1, l_compare)
    count_appearances = {}
    with open(out_filename, 'w') as outFile:
        for item_order in [ordered_lists.index(x) for x in lists]:
            if item_order in count_appearances:
                outFile.write(str(item_order +
                                  count_appearances[item_order]) + '\n')
                count_appearances[item_order] += 1
            else:
                outFile.write(str(item_order) + '\n')
                count_appearances[item_order] = 1
