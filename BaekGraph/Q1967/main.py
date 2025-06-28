import sys
import heapq

input = sys.stdin.readline

def dijkstra(start, adj):
    INF = float('inf')
    n = len(adj)
    dist = [INF]*n
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u].items():
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist

N = int(input())
adj = [dict() for _ in range(N+1)]
for _ in range(N-1):
    a,b,c = map(int, input().split())
    adj[a][b] = c
    adj[b][a] = c

# 1) 1번에서 가장 먼 노드 u 찾기 / 어느 값이든 상관은 없음
dist1 = dijkstra(1, adj)
u = max(range(1, N+1), key=lambda i: dist1[i])

# 2) u에서 다시 가장 먼 거리(지름) 구하기
distu = dijkstra(u, adj)
diameter = max(distu[1:])

print(diameter)
