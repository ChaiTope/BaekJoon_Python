import sys
import heapq

input = sys.stdin.readline

# 1) 입력
V = int(input())      # 정점 수
B = int(input())      # 간선(버스) 수

adj = [[] for _ in range(V+1)]
for _ in range(B):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))

start, end = map(int, input().split())

# 2) 다익스트라 함수
def dijkstra(start, adj):
    INF = float('inf')
    n = len(adj)
    dist = [INF] * n
    dist[start] = 0

    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist

# 3) 실행 후 결과 출력
dist = dijkstra(start, adj)
print(dist[end])
