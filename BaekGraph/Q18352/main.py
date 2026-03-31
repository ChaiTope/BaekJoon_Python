import sys
from collections import deque

input = sys.stdin.readline

N, M, K, X = map(int, input().split())
A = [[] for _ in range(N+1)]
dist = [-1 for _ in range(N+1)]
dist[X] = 0

for _ in range(M):
    a, b = map(int, input().split())
    A[a].append(b)

queue = deque()
queue.append(X)
while queue:
    x = queue.popleft()

    for v in A[x]:
        if dist[v] == -1:
            dist[v] = dist[x] + 1
            queue.append(v)

found = False

for i in range(1, N+1):
    if dist[i] == K:
        print(i)
        found = True

if not found:
    print(-1)