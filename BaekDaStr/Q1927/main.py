import sys
import heapq

input = sys.stdin.readline

N = int(input())
h = []
for i in range(N):
    n = int(input())
    if n == 0:
        if h:
            print(heapq.heappop(h))
        else:
            print(0)
    else:
        heapq.heappush(h, n)