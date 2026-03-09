import sys
import heapq
from collections import deque

input = sys.stdin.readline

INF = 10**18

def dijkstra(start, adj, removed, N):
    dist = [INF] * N
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        cost, u = heapq.heappop(pq)
        if cost != dist[u]:
            continue

        for v, w, eid in adj[u]:
            if removed[eid]:
                continue
            nc = cost + w
            if nc < dist[v]:
                dist[v] = nc
                heapq.heappush(pq, (nc, v))

    return dist

def mark_removed(dist, D, radj, removed, N):
    """
    D에서 역방향으로 BFS/큐 탐색.
    dist[prev] + w == dist[cur] 인 간선(prev->cur)은
    '어떤 최단경로'의 일부이므로 removed[eid]=True 처리.
    """
    q = deque([D])
    seen = [False] * N
    seen[D] = True

    while q:
        cur = q.popleft()

        for prev, w, eid in radj[cur]:
            # 최단경로 간선 조건
            if dist[prev] + w == dist[cur]:
                if not removed[eid]:
                    removed[eid] = True
                if not seen[prev]:
                    seen[prev] = True
                    q.append(prev)

def solve_one_case(N, M):
    S, D = map(int, input().split())

    adj = [[] for _ in range(N)]
    radj = [[] for _ in range(N)]

    # 간선마다 고유 id 부여
    # removed[eid] 로 제거 여부 관리
    removed = [False] * M

    for eid in range(M):
        u, v, w = map(int, input().split())
        adj[u].append((v, w, eid))
        radj[v].append((u, w, eid))

    # 1) 최단거리
    dist1 = dijkstra(S, adj, removed, N)
    if dist1[D] >= INF:
        return -1

    # 2) 최단경로 간선들 제거 표시
    mark_removed(dist1, D, radj, removed, N)

    # 3) 제거 반영 후 다시 최단거리
    dist2 = dijkstra(S, adj, removed, N)
    return -1 if dist2[D] >= INF else dist2[D]

while True:
        N, M = map(int, input().split())
        if N == 0 and M == 0:
            sys.exit()
        ans = solve_one_case(N, M)
        print(ans)