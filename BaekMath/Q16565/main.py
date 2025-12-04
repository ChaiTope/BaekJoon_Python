import sys
from math import comb

input = sys.stdin.readline

N = int(input())
ans = 0
mod = 10007
for k in range(1, N//4 + 1):
    ans += ((-1)**(k-1) * comb(13, k) * comb(52 - 4*k, N - 4*k)) % mod

print(ans%mod)