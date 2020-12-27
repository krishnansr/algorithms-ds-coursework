import time
import numpy as np
import math, sys
from pprint import pprint
import heapq

# sys.setrecursionlimit(10**6)
print('The sys recursion limit is...', sys.getrecursionlimit())


def get_median(num):
    global heap_low_size
    global heap_high_size

    if heap_low_size < 1:
        heapq.heappush(heapLow, -num)
        heap_low_size += 1
        median_val = num

    else:
        if num < -heapLow[0]:
            heapq.heappush(heapLow, -num)
            heap_low_size += 1
        else:
            heapq.heappush(heapHigh, num)
            heap_high_size += 1

        # restructure heaps
        if heap_high_size - heap_low_size > 1:
            transfer_num = heapq.heappop(heapHigh)
            heapq.heappush(heapLow, -transfer_num)
            heap_high_size -= 1
            heap_low_size += 1
        elif heap_low_size - heap_high_size > 1:
            transfer_num = heapq.heappop(heapLow)
            heapq.heappush(heapHigh, -transfer_num)
            heap_low_size -= 1
            heap_high_size += 1

        # compute median value
        median_val = heapHigh[0] if heap_high_size > heap_low_size else -heapLow[0]

    return median_val


if __name__ == '__main__':
    file_name = 'medianMaintenanceData.txt'
    # file_name = 'medianMaintenanceTest2.txt'

    heapLow = list()
    heap_low_size = 0
    heapHigh = list()
    heap_high_size = 0
    # number_stream = list()

    median_values = list()
    with open(file_name) as f:
        for line in f:
            curr_num = int(line)
            median_val = get_median(curr_num)
            median_values.append(median_val)

            # for book-keeping
            # number_stream.append(curr_num)
            # print([ -x for x in heapLow ], heapHigh, median_val)

    print('The consecutive median values are...', median_values)
    print('The required final mod_sum value of medians is...', sum(median_values)%10000)