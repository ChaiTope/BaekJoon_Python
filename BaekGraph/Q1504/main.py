import sys
import heapq

input = sys.stdin.readline

N, E = map(int, input().split())

trunk = [dict() for _ in range(N+1)]

for i in range(E):
    a, b, c = map(int, input().split())

    trunk[a][b] = c
    trunk[b][a] = c

v1, v2 = map(int, input().split())

def dijkstra(start, adj):
    INF = float('inf')
    n = len(adj)               # 정점 수
    dist = [INF] * n
    dist[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))  # (거리, 정점)

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue  # 이미 더 짧은 경로가 발견된 상태

        for v, w in adj[u].items():
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))

    return dist

INF = float('inf')

dist1  = dijkstra(1,   trunk)
distV1 = dijkstra(v1,  trunk)
distV2 = dijkstra(v2,  trunk)

# 두 가지 후보 경로
path1 = dist1[v1] + distV1[v2] + distV2[N]   # 1 → v1 → v2 → N
path2 = dist1[v2] + distV2[v1] + distV1[N]   # 1 → v2 → v1 → N

res = min(path1, path2)
# 하나라도 INF 섞이면 res가 INF
print(res if res < INF else -1)