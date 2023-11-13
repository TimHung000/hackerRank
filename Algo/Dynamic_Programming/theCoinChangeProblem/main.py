# dp
def getWays(n, c):
    dp = [[0 for i in range(n+1)] for j in range(len(c))]
    for i in range(len(c)):
        dp[i][0] = 1
    
    for i in range(len(c)):
        for j in range(n+1):
            dp[i][j] = dp[i-1][j]
            if j - c[i] >= 0:
                dp[i][j] += dp[i][j-c[i]]
                                
    return dp[len(c)-1][n]

# recursion 
def helper(currentIdx, target, arr, memo):
    if target == 0:
        return 1
    if target < 0 or currentIdx < 0:
        return 0
    if memo[currentIdx][target] != -1:
        return memo[currentIdx][target]
    
    withCurrentIdx = helper(currentIdx, target-arr[currentIdx], arr, memo)
    withoutCurrentIdx = helper(currentIdx - 1, target, arr, memo)
    memo[currentIdx][target] = withCurrentIdx + withoutCurrentIdx

    return memo[currentIdx][target]

def getWays1(n, c):
    memo = [[-1] * (n + 1) for i in range(len(c))]
                                
    return helper(len(c)-1, n, c, memo)

if __name__ == '__main__':
    n = 3
    c = [8, 3, 1, 2]
    print(getWays(n, c))
    