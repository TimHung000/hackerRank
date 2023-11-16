#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridlandMetro' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER k
#  4. 2D_INTEGER_ARRAY track
#

def gridlandMetro(n, m, k, tracks):
    track.sort(key= lambda track: min(track[1], track[2]))

    rowLastCol = {}
    count = 0
    for r, c1, c2 in tracks:
        if c2 < c1:
            c1, c2 = c2, c1
        
        if not rowLastCol.get(r):
            rowLastCol[r] = c2
            count += c2 - c1 + 1
        else:
            if rowLastCol[r] < c1:
                rowLastCol[r] = c2
                count += c2 - c1 + 1
            elif rowLastCol[r] < c2:
                count += c2 - rowLastCol[r]
                rowLastCol[r] = c2

    res = n * m - count
    return res

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    track = []

    for _ in range(k):
        track.append(list(map(int, input().rstrip().split())))

    result = gridlandMetro(n, m, k, track)

    print(str(result) + '\n')