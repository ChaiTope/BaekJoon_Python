import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
visited = [False]*(n+1)
P = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    P[x].append(y)
    P[y].append(x)

def bfs(a, b):
    visited = [False]*(n+1)
    q = deque([(a,0)])
    visited[a] = True

    while q:
        node, dist = q.popleft()

        if node == b:
            return dist

        for p in P[node]:
            if not visited[p]:
                visited[p] = True
                q.append((p, dist+1))

    return -1

print(bfs(p1, p2))
