#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumLoss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY price as parameter.
#
def minimumLoss(price):
    priceIdxMap = dict([(val, idx) for idx, val in enumerate(price)])
    
    price.sort(reverse=True)
    minLoss = float('inf')
    for i in range(len(price)-1):
        j = i + 1
        while j < len(price) and priceIdxMap[price[j]] < priceIdxMap[price[i]]:
            j += 1
        
        if j < len(price) and price[i] - price[j] < minLoss:
            minLoss = price[i] - price[j]

    return minLoss

# time
def minimumLoss(price):
    prev = []
    res = float('inf')
    for p in price:
        for prevP in prev:
            loss = prevP - p
            if loss > 0 and loss < res:
                res = loss
        prev.append(p)
    return res

if __name__ == '__main__':

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    print(str(result) + '\n')
