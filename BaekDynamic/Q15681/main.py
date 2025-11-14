import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, R, Q = map(int, input().split())

graph = [[] for _ in range(N+1)]
size = [0 for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(u, parent):
    size[u] = 1
    for v in graph[u]:
        if v != parent:     # 부모로 역방향 가지 않기
            dfs(v, u)
            size[u] += size[v]

dfs(R, graph)

for _ in range(Q):
    u = int(input())

    print(size[u])