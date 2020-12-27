import numpy as np
from math import ceil, floor
import time
import sys

print('The sys recursion limit...', sys.getrecursionlimit())

def karats_mul(n1, n2):
    str_n1 = str(n1)
    str_n2 = str(n2)
    len1 = len(str_n1)
    len2 = len(str_n2)

    if len1 == 1 and len2 == 1:
        return n1*n2

    if len1 != 1:
        a, b = str_n1[:floor(len1/2)], str_n1[floor(len1/2):]
    else:
        a, b = 0, n1

    if len2 != 1:
        c, d = str_n2[:floor(len2/2)], str_n2[floor(len2/2):]
    else:
        c, d = 0, n2

    lenb, lend = len(str(b)), len(str(d))
    a, b, c, d = int(a), int(b), int(c), int(d)

    res = int(  karats_mul(a, c)*10**(lenb+lend) + karats_mul(b, d) \
               + karats_mul(a, d)*10**lenb + karats_mul(b, c)*10**lend )
    return res

num1 = 3141592653589793238462643383279502884197169399375105820974944592
num2 = 2718281828459045235360287471352662497757247093699959574966967627

s2 = time.time()
final_prod = karats_mul(num1, num2)
print(f'multiplying {num1} with {num2} \ngives......... {final_prod}, \nexpected is... {num1*num2}')
e2 = time.time()
time2 = (e2-s2)

print('multiply time is ', time2, final_prod == num1*num2)

