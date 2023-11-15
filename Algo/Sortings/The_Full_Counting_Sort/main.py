#!/bin/python3

import math
import os
import random
import re
import sys
import collections

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#
def countSort(arr):
    result = [[] for i in range(100)]
    n = len(arr)
    for i in range(n//2):
        result[int(arr[i][0])].append('-')

    for i in range(n//2, n):
        result[int(arr[i][0])].append(arr[i][1])

    for item in result:
        if item:
            print(*item, end=' ')

def countSort1(arr):
    n = len(arr)
    bucket = collections.defaultdict(list)
    for i in range(n//2):
        bucket[int(arr[i][0])].append('-')
            
    for i in range(n//2, n):
        bucket[int(arr[i][0])].append(arr[i][1])

    sorted_bucket = dict(sorted(bucket.items()))

    res = " ".join([" ".join(val) for val in sorted_bucket.values()])
    print(res)


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
