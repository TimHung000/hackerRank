#!/bin/python3

import math
import os
import random
import re
import sys

# dp
def cost(B):
    # dp[0][j] : maximum possible absolute difference till index j if the jth element is chosen to be B[j]
    # dp[1][j] : maximum possible absolute difference till index j if the jth element is chosen to be 1
    dp = [[0] * len(B) for _ in range(2)]
    for idx in range(1, len(B)):
        dp[0][idx] = max(dp[0][idx-1] + abs(B[idx] - B[idx-1]), dp[1][idx-1] + abs(B[idx] - 1)) 
        dp[1][idx] = max(dp[0][idx-1] + abs(1 - B[idx-1]), dp[1][idx-1]) 
    return max(dp[0][len(B)-1], dp[1][len(B)-1])

# recursion + memoize 
def helper(currentIdx, B, memo, nextVal):
    if currentIdx < 0:
        return 0
    tmp1 = helper(currentIdx-1, B, memo, B[currentIdx]) if memo[0][currentIdx] == -1 else memo[0][currentIdx]
    tmp2 = helper(currentIdx-1, B, memo, 1) if memo[1][currentIdx] == -1 else memo[1][currentIdx]
    memo[0][currentIdx] = tmp1
    memo[1][currentIdx] = tmp2

    tmp1 += abs(nextVal - B[currentIdx])
    tmp2 += abs(nextVal - 1) 
    return max(tmp1, tmp2)

def cost1(B):
    memo = [[-1] * len(B) for i in range(2)]

    tmp1 = helper(len(B)-2, B, memo, B[len(B)-1])
    tmp2 = helper(len(B)-2, B, memo, 1)
    return max(tmp1, tmp2)


if __name__ == '__main__':
    B = [10, 1, 10, 1, 10]
    print(cost(B))
