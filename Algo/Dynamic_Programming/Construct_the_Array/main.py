# solution reference : https://thalaivar.github.io/posts/2021/03/19/bottom_up_dp_1　

# O(nk^2)
def countArray(n, k, x):
    # dp[i][j] : the number of ways an array of length i + 1 can be constructed, such that it ends in j + 1.
    dp = [[0] * k for _ in range(n)]
    # only one way to make array of length 1
    dp[0][0] = 1

    for i in range(1, n):
        for j in range(k):
            dp[i][j] = sum(dp[i-1]) - dp[i-1][j]
        
    return dp[n-1][x-1] % ((10 ** 9) + 7)

# O(nk^2)
def countArray(n, k, x):
    dp = [0] * k
    dp[0] = 1
    for i in range(1, n):
        dp = [sum(dp) - prev for prev in dp]
    return dp[x-1] % ((10 ** 9) + 7)

'''
k = 4

1th-iteration    [1, 0, 0, 0]
2th-iteration    [0, 1, 1, 1]
3th-iteration    [3, 2, 2, 2]
4th-iteration    [6, 7, 7, 7]
5th-iteration    [21, 20, 20, 20]

clearly, dp[i][j] are the same for j = 1~k-1
Thus, we only need a 1*2 array to find the answer.

dp[0] = (k-1) * dp[1]
dp[1] = (k-2) * dp[1] + dp[0]
'''
def countArray(n, k, x):
    dp = [1, 0]
    for i in range(1, n):
        dp[0], dp[1] = (k-1) * dp[1], (k-2) * dp[1] + dp[0]
    res = dp[0] if x == 1 else dp[1]
    return res % ((10 ** 9) + 7)


if __name__ == '__main__':
    test1 = countArray(4, 3, 2)
    print(test1)