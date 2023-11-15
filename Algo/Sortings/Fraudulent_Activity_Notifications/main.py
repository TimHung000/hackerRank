#!/bin/python3

import math
import os
import random
import re
import sys
import math
import bisect

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#
def binarySearch(arr, val):
    l, r = 0, len(arr)-1
    m = 0
    while l < r:
        m = (l + r) // 2
        if val < arr[m]:
            r = m - 1
        elif val > arr[m]:
            l = m + 1
        else:
            return m
    
    if val >= arr[l]:
        return l + 1
    else:
        return l
    
def countSort(arr):
    bucket = [0] * (max(arr) + 1)
    res = []
    for i in range(len(arr)):
        bucket[arr[i]] += 1
    
    for i in range(len(bucket)):
        res.extend([i] * bucket[i])
    return res


def findLimit(bucket, d):
    idx1 = (d + 1) // 2
    idx2 = d // 2 + 1 
    prevCount = 0
    curCount = 0
    for exp in range(len(bucket)):
        prevCount = curCount
        curCount += bucket[exp]
        if idx1 > prevCount and idx1 <= curCount:
            median1 = exp
        if idx2 > prevCount and idx2 <= curCount:
            median2 = exp
            break
    return median1 + median2

def activityNotifications(expenditure, d):
    res = 0
    bucket = [0] * 201
    for i in range(d):
        bucket[expenditure[i]] += 1

    for i in range(d, len(expenditure)):
        if expenditure[i] >= findLimit(bucket, d):
            res += 1      
        bucket[expenditure[i-d]] -= 1
        bucket[expenditure[i]] += 1

    return res


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    print(str(result) + '\n')
