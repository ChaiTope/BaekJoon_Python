import sys

input = sys.stdin.readline
INF = 10**15

N, M = map(int, input().split())
edges = []

for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    edges.append((a, b, c))

dist = [INF] * N
dist[0] = 0

# N-1번 완화
for _ in range(N - 1):
    updated = False
    for u, v, w in edges:
        if dist[u] != INF and dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            updated = True
    if not updated:
        break

# 음수 사이클 검사
for u, v, w in edges:
    if dist[u] != INF and dist[v] > dist[u] + w:
        print(-1)
        break
else:
    for i in range(1, N):
        print(dist[i] if dist[i] != INF else -1)