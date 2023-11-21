#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'journeyToMoon' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY astronaut
#

def journeyToMoon(n, astronaut):
    parents = list(range(n))
    rank = [1] * n
    size = [1] * n

    def find(node):
        if parents[node] != node:
            parents[node] = find(parents[node])
            size[node] = 1
        return parents[node]

    def union(node1, node2):
        root1 = find(node1)
        root2 = find(node2)

        if root1 != root2:
            if rank[root1] < rank[root2]:
                parents[root1] = root2
                size[root2] += size[root1]
            elif rank[root1] > rank[root2]:
                parents[root2] = root1
                size[root1] += size[root2]
            else:
                parents[root1] = root2
                rank[root2] += 1
                size[root2] += size[root1]

    for p1, p2 in astronaut:
        if find(p1) != find(p2):
            union(p1, p2)
    
    res = n * (n-1) // 2
    for i in range(n):
        if i == parents[i]:
            res -= size[i] * (size[i] - 1) // 2
    
    return res




if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    p = int(first_multiple_input[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    print(str(result) + '\n')
