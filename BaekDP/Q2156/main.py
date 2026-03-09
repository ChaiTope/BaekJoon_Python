import sys

input = sys.stdin.readline

N = int(input())
drink = [int(input()) for i in range(N)]

if N == 1:
    print(drink[0])
    sys.exit()
if N == 2:
    print(drink[0] + drink[1])
    sys.exit()

dp = [0] * N

dp[0] = drink[0]
dp[1] = drink[0] + drink[1]
dp[2] = max(dp[1], max(dp[0] + drink[2], drink[1] + drink[2]))

for n in range(3, N):
    dp[n] = max(dp[n-1], max(dp[n-2] + drink[n], dp[n-3]+drink[n-1]+drink[n]))

print(dp[N-1])