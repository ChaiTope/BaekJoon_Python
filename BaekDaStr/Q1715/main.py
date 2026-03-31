import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = [int(input()) for _ in range(N)]
heapq.heapify(heap)

res = 0

while len(heap) > 1:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    s = a + b
    res += s
    heapq.heappush(heap, s)

print(res)