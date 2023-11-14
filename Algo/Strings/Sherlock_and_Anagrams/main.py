#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s: str):
    strIntMap = {}
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substr = s[i:j]
            substr = ''.join(sorted(substr))
            strIntMap[substr] = strIntMap.get(substr, 0) + 1

    count = 0
    for val in strIntMap.values():
        # nC2 combinational rule
        count += (val * (val - 1) // 2)

    return count


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        print(str(result))

