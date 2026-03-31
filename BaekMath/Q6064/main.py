import math
import sys

input = sys.stdin.readline

T = int(input())
for i in range(T):
    M, N, x, y = map(int, input().split())
    k = x

    limit = math.lcm(M, N)

    while k <= limit:
        if k % N == y % N:
            print(k)
            break
        k += M
    else:
        print(-1)