import sys

input = sys.stdin.readline

N = int(input())

dp = [0] * max(3,(N + 1))
dp[0] = 0
dp[1] = 1
dp[2] = 2

mod = 10**4 + 7
for i in range(3, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
    dp[i] %= mod

print(dp[N])