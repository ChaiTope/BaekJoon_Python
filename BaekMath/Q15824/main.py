import sys

input = sys.stdin.readline

N = int(input())
mod = 10 ** 9 + 7
arr = sorted(list(map(int, input().split())))

# 2^i 미리 계산
pow2 = [1] * N
for i in range(1, N):
    pow2[i] = (pow2[i-1] * 2) % mod

res = 0
for i in range(N):
    diff = (pow2[i] - pow2[N-1-i]) % mod
    res = (res + arr[i] * diff) % mod

print(res)