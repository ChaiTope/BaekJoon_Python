import sys

input = sys.stdin.readline

T = int(input())

dp = [[1] * 14 for i in range(15)]

for i in range(14):
    dp[0][i] = i + 1

for i in range(1, 15):
    for j in range(1, 14):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

for i in range(T):
    k = int(input())
    n = int(input())

    print(dp[k][n-1])