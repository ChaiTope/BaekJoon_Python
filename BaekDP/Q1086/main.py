import sys
import math
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]

K = int(input())
mod_val = [0] * (N + 1)
pre_pow = [0] * (N + 1)

for i in range(N):
    x = arr[i]
    mod_val[i] = x % K
    pre_pow[i] = pow(10, len(str(x)), K)

dp = [[0] * K for _ in range(1<<N)]

dp[0][0] = 1

for mask in range(1<<N):
    for r in range(K):
        if dp[mask][r] == 0:
            continue

        for j in range(N):
            if (mask & (1<<j)) == 0:      # j를 아직 안 썼다면
                next_mask = mask | (1<<j)

                next_r = (r * pre_pow[j] + mod_val[j]) % K

                dp[next_mask][next_r] += dp[mask][r]

full_mask = (1<<N) - 1
p = dp[full_mask][0]
q = math.factorial(N)
g = math.gcd(p, q)

print(p//g, "/", q//g, sep='')