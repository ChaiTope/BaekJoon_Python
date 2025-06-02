from collections import deque

N, M, V = map(int, input().split())

way = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())

    way[a].append(b)
    way[b].append(a)

for i in range(1, N+1):
    way[i].sort()

visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)

def dfs(start, path):
    visited_dfs[start] = True
    path.append(start)

    for v in way[start]:
        if not visited_dfs[v]:
            dfs(v, path)

def bfs(start, order):
    queue = deque([start])
    visited_bfs[start] = True

    while queue:
        cur = queue.popleft()
        order.append(cur)

        for nxt in way[cur]:
            if not visited_bfs[nxt]:
                visited_bfs[nxt] = True
                queue.append(nxt)

dfs_order = []
bfs_order = []

dfs(V, dfs_order)
bfs(V, bfs_order)

print(*dfs_order)  # 공백으로 구분해서 출력
print(*bfs_order)