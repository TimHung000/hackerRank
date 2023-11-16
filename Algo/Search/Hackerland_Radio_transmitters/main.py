#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerlandRadioTransmitters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER k
#

def hackerlandRadioTransmitters(x, k):
    x.sort()
    res = 0

    n = len(x)
    i = 0
    while i < n:
        loc = x[i] + k
        while i < n and x[i] <= loc:
            i += 1
        i -= 1
        res += 1

        loc = x[i] + k
        while i < n and x[i] <= loc:
            i += 1
    return res

def hackerlandRadioTransmitters1(x, k):
    res = 0
    x.sort()
    prevLandLoc = []
    curRadioPos = -k 
    for loc in x:
        if len(prevLandLoc) > 0 and loc - prevLandLoc[0] > k:
           res += 1
           curRadioPos = prevLandLoc[len(prevLandLoc)-1]
           prevLandLoc = []

        if loc <= curRadioPos + k:
            continue

        prevLandLoc.append(loc)

    if len(prevLandLoc) > 0:
        res += 1
    
    return res

def hackerlandRadioTransmitters(x, k):
    x.sort()
    res = 0

    n = len(x)
    i = 0
    while i < n:
        loc = x[i] + k
        while i < n and x[i] <= loc:
            i += 1
        i -= 1
        res += 1

        loc = x[i] + k
        while i < n and x[i] <= loc:
            i += 1
    return res

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    print(str(result) + '\n')