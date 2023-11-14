import math


def helper(currentVal, target, power):
    if target == 0:
        return 1
    if target < 0 or currentVal ** power > target:
        return 0
    
    notIncludeCurrent = helper(currentVal+1, target, power)
    includeCurrent = helper(currentVal+1, target - currentVal ** power, power)
    return notIncludeCurrent + includeCurrent

def powerSum(X, N):

    return helper(1, X, N)

if __name__ == '__main__':
    print(powerSum(10, 2))