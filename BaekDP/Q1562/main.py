import sys

input = sys.stdin.readline

N = int(input())
MOD = 10**9
dp = [[0]*(1<<10) for _ in range(10)]

for d in range(1, 10):
    dp[d][1 << d] = 1

for length in range(2, N+1):
    ndp = [[0]*(1<<10) for _ in range(10)]

    for last in range(10):
        for mask in range(1<<10):
            if dp[last][mask] == 0:
                continue

            for nxt in (last-1, last+1):
                if 0 <= nxt <= 9:
                    nmask = mask | (1 << nxt)
                    ndp[nxt][nmask] += dp[last][mask]
                    ndp[nxt][nmask] %= MOD

    dp = ndp

FULL = (1<<10) - 1
answer = 0

for last in range(10):
    answer = (answer + dp[last][FULL]) % MOD

print(answer)