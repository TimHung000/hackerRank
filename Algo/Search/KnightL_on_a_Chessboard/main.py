#!/bin/python3

import math
import os
import random
import re
import sys
import collections

#
# Complete the 'knightlOnAChessboard' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts INTEGER n as parameter.
#

def knightL(i, j, n):
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    dp[0][0] = 0
    queue = collections.deque([(0, 0)])

    while len(queue) != 0:
        r, c = queue.popleft()

        for moveR, moveC in [(i, j), (-i, j), (i, -j), (-i, -j), (j, i), (-j, i), (j, -i), (-j, -i)]:
            newR = r + moveR
            newC = c + moveC
            if newR < 0 or newR >= n:
                continue

            if newC < 0 or newC >= n:
                continue
            
            if dp[newR][newC] != -1:
                continue
            
            dp[newR][newC] = dp[r][c]+1
            queue.append((newR, newC))
            
    return dp[n-1][n-1]
    
def knightlOnAChessboard(n):
    res = []
    for i in range(n-1):
        row = []
        for j in range(n-1):
            row.append(knightL(i+1, j+1, n))
        res.append(row)

    return res


if __name__ == '__main__':

    n = int(input().strip())

    result = knightlOnAChessboard(n)

    print('\n'.join([' '.join(map(str, x)) for x in result]))
