import sys

input = sys.stdin.readline

N = int(input())

dp = [0] * (N+5)
t = [0] * (N+5)
p = [0] * (N+5)

for i in range(1, N+1):
    t[i], p[i] = map(int, input().split())

    dp[i] = max(dp[i], dp[i-1])
    if i + t[i] <= N+1:
        dp[i + t[i]] = max(dp[i + t[i]], dp[i] + p[i])

dp[N+1] = max(dp[N+1], dp[N])
print(dp[N+1])