#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def lilysHomework(arr):
    n = len(arr)
    arrValIdxMap = dict([(val, idx) for idx, val in enumerate(arr)])
    sortedArr = sorted(arr)



    sortedIdx = [arrValIdxMap[val] for val in sortedArr]
    resAscending = 0
    i = 0
    while i < n:
        if sortedIdx[i] > 0:
            # this is like moving the sorted to the
            sortedIdx[sortedIdx[i]], sortedIdx[i] = sortedIdx[i], sortedIdx[sortedIdx[i]]
            resAscending += 1


def lilysHomework(arr):


    arrCopy = arr[:]
    arrValIdxMap = dict([(val, idx) for idx, val in enumerate(arrCopy)])
    sortedArr = sorted(arrCopy)
    resAscending = 0
    for i in range(len(arrCopy)):
        if sortedArr[i] != arrCopy[i]:
            resAscending += 1
            arrIdx = arrValIdxMap[sortedArr[i]]
            arrValIdxMap[arrCopy[i]] = arrIdx
            arrCopy[i], arrCopy[arrIdx] = arrCopy[arrIdx], arrCopy[i]

    arrCopy = arr[:]
    arrValIdxMap = dict([(val, idx) for idx, val in enumerate(arrCopy)])
    sortedArr = sorted(arrCopy, reverse=True)
    resDescending = 0
    for i in range(len(arrCopy)):
        if sortedArr[i] != arrCopy[i]:
            resDescending += 1
            arrIdx = arrValIdxMap[sortedArr[i]]
            arrValIdxMap[arrCopy[i]] = arrIdx
            arrCopy[i], arrCopy[arrIdx] = arrCopy[arrIdx], arrCopy[i]

    return min(resAscending, resDescending)


if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    print(result)