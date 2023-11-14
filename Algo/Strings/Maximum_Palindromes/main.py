#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'initialize' function below.
#
# The function accepts STRING s as parameter.
#

myString: str = None
M = 1000000007
factorial = None
inverse_factorial = None
cnt = None

def initialize(s):
    global myString 
    global factorial
    global inverse_factorial
    global cnt
    myString = s
    factorial = [0] * (len(s) + 1)
    inverse_factorial = [0] * (len(s) + 1)
    factorial[0] = 1
    inverse_factorial[0] = 1
    for i in range(1, len(s) + 1):
        factorial[i] = (factorial[i-1] * i) % M
        # check Fermat's Little Theorem
        # a^(p-1) = 1 (mod p) if p is prime number and a is an integer not divisible by p
        # a * a^(p-2) = 1 (mod p) 
        # Now, let's say you have some number b and you want to fin b^-1 (the modular inverse of b) modulo p
        # b^-1 = b^(p-2) (mod p)
        inverse_factorial[i] = pow(factorial[i], M-2, M)
    
    cnt = [[0 for _ in range(len(s)+1)] for _ in range(26)]
    for i in range(1, len(s)+1):
        for j in range(26):
            cnt[j][i] += cnt[j][i-1]
        cnt[ord(s[i-1]) - ord('a')][i] += 1 


#
# Complete the 'answerQuery' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#

def answerQuery(l, r):
    numeratoer_factorial = 0
    denominator_factorial = 1
    middle_count = 0
    for i in range(26):
        val = cnt[i][r] - cnt[i][l-1]
        numeratoer_factorial += val // 2
        denominator_factorial = (denominator_factorial * inverse_factorial[val // 2]) % M
        middle_count += val % 2

    res = (factorial[numeratoer_factorial] * denominator_factorial) % M

    if middle_count != 0:
        res = res * middle_count % M
    return int(res)

if __name__ == '__main__':
    s = input()

    initialize(s)

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        l = int(first_multiple_input[0])

        r = int(first_multiple_input[1])

        result = answerQuery(l, r)

        print(result)

