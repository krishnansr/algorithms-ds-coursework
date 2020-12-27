import numpy as np
import time
import sys

print('The sys recursion limit...', sys.getrecursionlimit())

def selection_sort(inp):
    if len(inp) < 2:
        return inp

    min_ind = inp.index(min(inp))
    if min_ind != 0:
        inp[0], inp[min_ind] = inp[min_ind], inp[0]
    return inp[:1] + selection_sort(inp[1:])

def merge_sort(inp):
    if len(inp) < 2:
        return inp

    first, second = merge_sort(inp[::2]), merge_sort(inp[1::2])
    sorted = list()
    while first and second:
        if first[0] < second[0]:
            sorted.append(first.pop(0))
        else:
            sorted.append(second.pop(0))
    sorted.extend([*first, *second])
    return sorted

for i in range(1):
    inp = np.random.randint(0, 10000, 998).tolist()
    # inp = [1,5,2,7,3,4,8,6]

    s1 = time.time()
    native_sort = sorted(inp.copy())
    e1 = time.time()
    time1 = (e1-s1)
    print('\nnative......', time1)

    s2 = time.time()
    merge_output = merge_sort(inp.copy())
    e2 = time.time()
    time2 = (e2-s2)
    print('merge.......', time2)

    s3 = time.time()
    selection_output = selection_sort(inp.copy())
    e3 = time.time()
    time3 = (e3 - s3)
    print('selection...', time3)


    if selection_output != sorted(inp):
        print('noooo! '*20)
        break