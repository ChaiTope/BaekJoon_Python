import heapq
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

adj = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))

start, end = map(int, input().split())

def dijkstra(start, adj):
    INF = float('inf')
    n = len(adj)
    dist = [INF] * n
    dist[start] = 0
    prev = [-1] * n

    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                prev[v] = u
                heapq.heappush(pq, (nd, v))

    return dist, prev

# 3) 실행 후 결과 출력
dist, prev = dijkstra(start, adj)
print(dist[end])

# 경로 복원
path = []
cur = end
while cur != -1:
    path.append(cur)
    cur = prev[cur]
path.reverse()

# 경로 길이 + 실제 경로
print(len(path))
print(*path)