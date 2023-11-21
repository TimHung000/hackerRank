#!/bin/python3

import math
import os
import random
import re
import sys
import collections

#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#

def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib < c_road:
        return n * c_lib
    
    visited = [False] * n
    roadMap = collections.defaultdict(list)
    res = 0

    for start, end in cities:
        roadMap[start].append(end)
        roadMap[end].append(start)

    
    for city in range(1, n+1):
        if visited[city-1] is True:
            continue
        res += c_lib

        queue = collections.deque([city])
        while queue:
            curCity = queue.popleft()
            if visited[curCity-1]:
                continue

            for neighbor in roadMap[curCity]:
                if not visited[neighbor-1]:
                    queue.append(neighbor)

            res += c_road
            visited[curCity-1] = True
        res -= c_road
    return res
            


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        print(str(result) + '\n')

