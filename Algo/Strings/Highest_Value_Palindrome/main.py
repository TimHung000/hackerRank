#!/bin/python3


#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#

def highestValuePalindrome(s, n, k):
    sList = [*s]
    change = set()
    l, r = 0, n - 1
    while l < r:
        if sList[l] > sList[r]:
            change.add(r)
            k -= 1
            sList[r] = sList[l]
        elif sList[l] < sList[r]:
            change.add(l)
            k -= 1
            sList[l] = sList[r]
        l += 1
        r -= 1

    if k < 0:
        return '-1'
    
    l, r = 0, n - 1
    while l <= r and k > 0:
        if sList[l] != '9' and (l in change or r in change) and k >= 1:
            sList[l] = sList[r] = '9'
            k -= 1
        elif sList[l] != '9' and k >= 2:
            sList[l] = sList[r] = '9'
            k -= 2
        elif l == r and k >= 1:
            sList[l] = '9'
            k -= 1
        l += 1
        r -= 1

    return ''.join(sList)

        

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    print(result)