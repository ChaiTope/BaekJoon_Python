import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = int(input())
LOG = N.bit_length()  # 또는 math.ceil(math.log2(N)) + 1

adj = [[] for _ in range(N + 1)]
depth = [0] * (N + 1)
dist = [0] * (N + 1)
parent = [[0] * (N + 1) for _ in range(LOG)]

# 간선 입력 (N-1개)
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))

def dfs(cur, par):
    for (nxt, w) in adj[cur]:
        if nxt == par:
            continue
        depth[nxt] = depth[cur] + 1
        dist[nxt] = dist[cur] + w
        parent[0][nxt] = cur
        dfs(nxt, cur)

# 1번을 루트로 두고 DFS
depth[1] = 0
dist[1] = 0
parent[0][1] = 0
dfs(1, 0)

# parent 테이블 채우기
for k in range(1, LOG):
    for v in range(1, N + 1):
        parent[k][v] = parent[k - 1][ parent[k - 1][v] ]

def lca(a, b):
    # 깊이 맞추기
    if depth[a] < depth[b]:
        a, b = b, a

    diff = depth[a] - depth[b]
    for k in range(LOG):
        if diff & (1 << k):
            a = parent[k][a]

    if a == b:
        return a

    # 위에서부터 같이 점프
    for k in range(LOG - 1, -1, -1):
        if parent[k][a] != parent[k][b]:
            a = parent[k][a]
            b = parent[k][b]

    return parent[0][a]

M = int(input())

for i in range(M):
    a, b = map(int, input().split())
    c = lca(a, b)
    ans = dist[a] + dist[b] - 2 * dist[c]

    print(ans)