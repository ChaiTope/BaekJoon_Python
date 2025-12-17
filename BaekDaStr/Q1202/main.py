import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())

jewelries = []
bags = []
for _ in range(N):
    a, b = map(int, input().split())

    jewelries.append((a, b))

for _ in range(K):
    bags.append(int(input()))

jewelries.sort()
bags.sort()

max_heap = []
idx = 0
summary = 0

for bag in bags:
    while idx < len(jewelries) and jewelries[idx][0] <= bag:
        heapq.heappush(max_heap, -jewelries[idx][1])
        idx += 1

    if max_heap:
        summary += -heapq.heappop(max_heap)

print(summary)