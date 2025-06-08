import heapq
import sys

input = sys.stdin.readline
N = int(input())
h = []
for x in range(N):
    n = int(input())
    if n == 0:
        if h:
            print(heapq.heappop(h)[1])
        else:
            print(0)
    else:
        heapq.heappush(h, (abs(n), n))