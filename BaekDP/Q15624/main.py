import sys
input = sys.stdin.readline

MOD = 10**9 + 7
N = int(input())

a, b = 0, 1
for _ in range(N):
    a, b = b, (a + b) % MOD

print(a)
