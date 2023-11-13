
#!/bin/python3

import math
import os
import random
import re
import sys

def equal(arr):

    # we use the minimun value of array to be the first baseline, and try to make every item to be the same as its value
    # We can at most add 5 to item, so we use (min_num ~ min_num - 4) as the different baseline to find out how many steps
    # need to used in different baseline, and finally we select the min step in different basline
    min_num = min(arr)
    res = float('inf')
    for i in range(5):
        # add value to the n-1 items is like minus value to 1 item
        # so here we try to make every item to be the same as the minimum
        # store the total step in tmp[i]
        step = 0
        for val in arr:
            diff = val - (min_num - i)
            cur_step = diff // 5 + (diff % 5 // 2) + ((diff % 5) % 2)
            step += cur_step

        if step < res:
            res = step
    
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()