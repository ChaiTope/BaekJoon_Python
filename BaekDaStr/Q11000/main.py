import sys
import heapq

input = sys.stdin.readline
N = int(input())
S = sorted([list(map(int, input().split())) for _ in range(N)])
heap = [S[0][1]]
for i in range(1, N):
    if S[i][0] >= heap[0]:
        heapq.heappop(heap)
        heapq.heappush(heap, S[i][1])
    else:
        heapq.heappush(heap, S[i][1])

print(len(heap))