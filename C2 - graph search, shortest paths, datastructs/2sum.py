import time
import numpy as np
import math, sys
from pprint import pprint
import heapq

# sys.setrecursionlimit(10**6)
print('The sys recursion limit is...', sys.getrecursionlimit())

def target_present(neg_set, pos_set, target_sum, t_range):
    match_present = False
    for value in neg_set:
        expected_val = (target_sum-value)
        # if expected_val not in range(t_range[0], t_range[1]+1):
        #     continue
        if expected_val in pos_set:
            match_present = True
            break

    return match_present


if __name__ == '__main__':
    file_name = '2sum.txt'
    t_range = [-10000, 10000]
    # file_name = '2sumTest.txt'
    # t_range = [3, 10]

    with open(file_name) as f:
        int_stream = [int(v) for v in f.readlines()]
    print('chkpt 1: finished loading the integer stream')

    int_stream.sort()
    # print(int_stream)
    neg_ints = list(filter(lambda x:x<0, int_stream))
    pos_ints = list(filter(lambda x:x>0, int_stream))
    print(len(int_stream), len(pos_ints), len(neg_ints))
    print(max(neg_ints), min(pos_ints)) # -87405 112177
    print(neg_ints[-1], pos_ints[0]) # -87405 112177


    neg_set = set(neg_ints)
    pos_set = set(pos_ints)
    two_sum_count = 0
    start = time.time()
    for ind, target_t in enumerate(range(t_range[0], t_range[1]+1)):
        if target_present(neg_set, pos_set, target_t, t_range):
            two_sum_count += 1
        if ind%100 == 0:    # logging
            print(f'reached {round(ind*50/t_range[1], 4)}% values and {two_sum_count} values found...')

    end = time.time()
    print(f'chkpt 2: finished calculating the two sum count... {two_sum_count} in {round(end-start, 2)} seconds')
