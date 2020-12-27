import numpy as np
import time
import sys

print('The sys recursion limit is...', sys.getrecursionlimit())
count_comps = 0

def choose_pivot(inp, first, last):
    piv_method = 3
    if piv_method == 1:
        # always use the first element as the pivot element
        pass
    elif piv_method == 2:
        # always use the last element as the pivot element
        inp[first], inp[last] = inp[last], inp[first]
    elif piv_method == 3:
        # take the median of {first, middle, last} set as the pivot element
        middle = first + (last-first)//2
        pivot_set = {inp[first], inp[middle] ,inp[last]}
        median_val = sorted(pivot_set)[1]
        if median_val == inp[last]:
            inp[first], inp[last] = inp[last], inp[first]
        elif median_val == inp[middle]:
            inp[first], inp[middle] = inp[middle], inp[first]

def quick_sort_and_count_comps(inp, left, right):
    global count_comps
    count_comps += right-left-1

    if right-left < 3:
        if inp[left] > inp[left+1]:
            inp[left], inp[left+1] = inp[left+1], inp[left]
    else:
        # make the first element as pivot
        choose_pivot(inp, left, right-1)
        pivot = inp[left]
        i = left+1

        for j in range(left+1, right):
            if inp[j] < pivot:
                inp[i], inp[j] = inp[j], inp[i]
                i += 1
        inp[left], inp[i-1] = inp[i-1], inp[left]
        if i-left > 2:
            quick_sort_and_count_comps(inp, left, i-1)
        if right-i > 1:
            quick_sort_and_count_comps(inp, i, right)

if __name__ == '__main__':
    # file_name = 'QuickTest.txt'
    file_name = 'QuickSort.txt'

    with open(file_name) as f:
        inp = [ int(x) for x in f.readlines() ]

    s2 = time.time()
    quick_sort_and_count_comps(inp, 0, len(inp))
    print('Comparison counts...', count_comps)
    e2 = time.time()
    time2 = (e2-s2)
    print('quick sort time.......', time2)

