import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
M = int(input())

adj = [[] for _ in range(N+1)]
radj = [[] for _ in range(N+1)]
dist = [-1] * (N+1)
indegree = [0] * (N+1)

for i in range(M):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    radj[v].append((u, w))
    indegree[v] += 1

S, E = map(int, input().split())
dist[S] = 0

def topology_sort():
    q = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now=q.popleft()
        for nxt, w in adj[now]:
            if dist[now] != -1:
                dist[nxt] = max(dist[nxt], dist[now] + w)
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)

def reverse_trace():
    q = deque([E])
    visited = [False] * (N+1)
    visited[E] = True
    cnt = 0

    while q:
        cur = q.popleft()

        for prev, w in radj[cur]:
            # prev -> cur 가 최장경로 위에 있을 조건
            if dist[prev] != -1 and dist[prev] + w == dist[cur]:
                cnt += 1  # 간선은 조건 만족할 때마다 카운트

                if not visited[prev]:
                    visited[prev] = True
                    q.append(prev)

    return cnt

topology_sort()

print(dist[E])
print(reverse_trace())