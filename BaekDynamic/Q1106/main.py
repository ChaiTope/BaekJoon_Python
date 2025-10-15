import sys

input = sys.stdin.readline

C, N = map(int, input().split()) # 원하는 인원, 도시 수

cities = [tuple(map(int, input().split())) for _ in range(N)]

INF = 10**9
dp = [INF] * (C + 100)
dp[0] = 0

for cost, customer in cities:
    for i in range(customer, C + 100):
        dp[i] = min(dp[i], dp[i - customer] + cost)

print(min(dp[C:]))