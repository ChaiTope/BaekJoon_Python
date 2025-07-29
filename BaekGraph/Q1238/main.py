import sys
import heapq

input = sys.stdin.readline

N, M, X = map(int, input().split())

villages = [[] for _ in range(N + 1)]
reversed_villages = [[] for _ in range(N + 1)]

for i in range(1, M + 1):
    n1, n2, T = map(int, input().split())

    villages[n1].append((n2, T))
    reversed_villages[n2].append((n1, T))

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

    return dist

go = dijkstra(X, villages)
back = dijkstra(X, reversed_villages)
longest = 0

for i in range(1, N + 1):
     longest = max(longest, (go[i] + back[i]))

print(longest)