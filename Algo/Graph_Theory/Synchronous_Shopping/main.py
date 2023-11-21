#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'shop' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. STRING_ARRAY centers
#  4. 2D_INTEGER_ARRAY roads
#

class Graph():
    def __init__(self, n):
        self.shops = n
        self.ajacencyList = [[] for _ in range(n+1)]
        self.fishByShop = [0 for _ in range(n+1)]

    def addEdge(self, v1, v2, weight):
        self.ajacencyList[v1].append((v2, weight))
        self.ajacencyList[v2].append((v1, weight))

    def addFish(self, shop, fish):
        self.fishByShop[shop] |= 1 << fish

    def dijkstra(self, k):
        dist = [[float('inf') for _ in range((1 << k + 1))] for _ in range(self.shops + 1)]
        dist[1][self.fishByShop[1]] = 0
        
        # (distance, accuFish, curShop)
        pq = [(0, self.fishByShop[1], 1)]
        while pq:
            distance, accuFish, curShop = heapq.heappop(pq)
            if dist[curShop][accuFish] == float('inf'):
                continue

            for neighborShop, edgeWeight in self.ajacencyList[curShop]:
                newFish = accuFish | self.fishByShop[neighborShop]
                if dist[neighborShop][newFish] > distance + edgeWeight:
                    dist[neighborShop][newFish] = distance + edgeWeight
                    heapq.heappush(pq, (dist[neighborShop][newFish], newFish, neighborShop))

        res = float('inf')
        for i in range(1 << k + 1):
            for j in range(1 << k + 1):
                if i | j == (1 << k + 1) - 2:
                    res = min(res, max(dist[self.shops][i], dist[self.shops][j]))
                
        return res

def shop(n, k, centers, roads):
    myGraph = Graph(n)
    for v1, v2, weight in roads:
        myGraph.addEdge(v1, v2, weight)
    
    for idx, center in enumerate(centers):
        items = list(map(int, center.rstrip().split(' ')))
        for fish in items[1:]:
            myGraph.addFish(idx+1, fish)

    return myGraph.dijkstra(k)
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    centers = []

    for _ in range(n):
        centers_item = input()
        centers.append(centers_item)

    roads = []

    for _ in range(m):
        roads.append(list(map(int, input().rstrip().split())))

    res = shop(n, k, centers, roads)

    print(str(res) + '\n')
