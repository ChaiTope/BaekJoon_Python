import sys
import heapq

input = sys.stdin.readline

V = int(input())
tree = [[] for _ in range(V + 1)]

for i in range(V):
    nodes = list(map(int, input().split()))
    node = nodes[0]

    for j in range(1, len(nodes), 2):
        if nodes[j] == -1:
            break

        tree[node].append([nodes[j], nodes[j+1]])

def dijkstra(start, adj):
    INF = float('inf')
    n = len(adj)               # 정점 수
    dist = [INF] * n
    dist[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))  # (거리, 정점)
    loc = 0
    max_val = 0
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue

        # 여기서 '확정'이 됐으니 이때 갱신
        loc = u
        max_val = d

        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))

    return loc, max_val

ch, ch_res = dijkstra(1, tree)
adj, res = dijkstra(ch, tree)

print(res)
