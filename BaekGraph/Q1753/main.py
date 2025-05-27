import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())

K = int(input())

nodes = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    nodes[u].append((v, w))

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

        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))

    for d in dist[1:]:
        print(d if d != INF else "INF")

    return dist

dijkstra(K, nodes)