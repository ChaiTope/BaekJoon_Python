import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
visited = [False for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(start, depth):
    if depth == 5:
        print(1)
        sys.exit(0)

    for v in graph[start]:
        if not visited[v]:
            visited[v] = True
            dfs(v, depth + 1)
            visited[v] = False

for i in range(N):
    visited[i] = True
    dfs(i, 1)
    visited[i] = False

print(0)