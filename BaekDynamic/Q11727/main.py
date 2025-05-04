import sys

input = sys.stdin.readline

N = int(input())

a, b = 1, 3

mod = 10**4 + 7

if N == 0:
    print(0)
elif N == 1:
    print(1)
else:
    for i in range(2, N):
        a, b = b, (a + a + b) % mod
    print(b)