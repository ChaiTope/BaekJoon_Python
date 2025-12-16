import sys

input = sys.stdin.readline

INF = float('inf')
N = int(input())
r = [0] * (N + 1)
c = [0] * (N + 1)
dp = [[INF]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    a, b = map(int, input().split())
    r[i], c[i] = a, b
    dp[i][i] = 0

for length in range(2, N+1):
    for i in range(1, N - length + 2):
        j = i + length - 1
        dp[i][j] = INF
        for k in range(i, j):
            cost = dp[i][k] + dp[k + 1][j] + r[i] * c[k] * c[j]
            dp[i][j] = min(dp[i][j], cost)

print(dp[1][N])