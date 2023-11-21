#!/bin/python3

import math
import os
import random
import re
import sys
import collections

#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#

def bfs(n, m, edges, s):
    adjencyList = [[] for _ in range(n)]
    for i in range(m):
        node1, node2 = edges[i]
        adjencyList[node1-1].append(node2-1)
        adjencyList[node2-1].append(node1-1)
    
    dist = [-1] * n
    dist[s-1] = 0
    queue = collections.deque([s-1])
    while queue:
        node = queue.popleft()
        for neighbor in adjencyList[node]:
            if dist[neighbor] != -1:
                continue
            dist[neighbor] = dist[node] + 6
            queue.append(neighbor)
        
    res = dist[:s-1] + dist[s:]
    return res

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        print(' '.join(map(str, result)))

