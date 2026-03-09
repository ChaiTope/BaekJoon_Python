import math
import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    n, m = map(int, input().split())
    d = m - n
    k = math.floor(math.sqrt(d))

    if d == k * k:
        print(2 * k - 1)
    elif d <= k * k + k:
        print(2 * k)
    else:
        print(2 * k + 1)