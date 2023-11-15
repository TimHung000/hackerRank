#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    sorted_arr = sorted(arr)
    res = []
    min_diff = sorted_arr[1] - sorted_arr[0]
    for val1, val2 in zip(sorted_arr[:-1], sorted_arr[1:]):
        if val2 - val1 == min_diff:
            res.extend([val1, val2])
        if val2 - val1 < min_diff:
            res = [val1, val2]
            min_diff = val2 - val1
    return res

if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    print(' '.join(map(str, result)))

