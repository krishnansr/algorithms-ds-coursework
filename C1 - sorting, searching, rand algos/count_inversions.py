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

    # different breaking algorithm here instead of breaking into left & right half
    first, second = merge_sort(inp[::2]), merge_sort(inp[1::2])
    res_sorted = list()
    while first and second:
        if first[0] <= second[0]:
            res_sorted.append(first.pop(0))
        else:
            res_sorted.append(second.pop(0))
    res_sorted.extend([*first, *second])
    return res_sorted


def merge_sort_and_count_inv(inp):
    if len(inp) < 2:
        return 0, inp

    count_first, first = merge_sort_and_count_inv(inp[:len(inp)//2])
    count_second, second = merge_sort_and_count_inv(inp[len(inp)//2:])

    count_inv = 0
    res_sorted = list()
    while first and second:
        if first[0] <= second[0]:
            res_sorted.append(first.pop(0))
        else:
            # print(first[0], second[0], len(first))
            res_sorted.append(second.pop(0))
            count_inv += len(first)
    res_sorted.extend([*first, *second])
    return count_first+count_second+count_inv, res_sorted

for i in range(1):
    # file_name = 'IntegerTest.txt'
    file_name = 'IntegerArray.txt'

    # inp = np.random.randint(0, 10000, 998).tolist()
    # inp = [1,5,2,7,3,4,8,6]
    # inp = [2,4,1,3,5] #3 ->  (2, 1), (4, 1), (4, 3)

    with open(file_name) as f:
        inp = [ int(x) for x in f.readlines()]

    s2 = time.time()
    count_inv, merge_output = merge_sort_and_count_inv(inp.copy())
    print('Inversion counts...', count_inv)
    # print(merge_output)
    e2 = time.time()
    time2 = (e2-s2)
    print('merge time.......', time2)

