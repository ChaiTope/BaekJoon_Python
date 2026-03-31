import sys

input = sys.stdin.readline

INF = float('inf')
n, k = map(int, input().split())
coins = []
dp = [INF] * (k + 1)
dp[0] = 0

for _ in range(n):
    coin = int(input())
    coins.append(coin)

coins = sorted(set(coins))

for i in range(1, k + 1):
    for coin in coins:
        if i >= coin:
            dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[k] == INF:
    print(-1)
else:
    print(dp[k])