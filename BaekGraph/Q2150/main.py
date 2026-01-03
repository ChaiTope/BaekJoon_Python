import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

V, E = map(int, input().split())
nodes = [[] for _ in range(V + 1)]

for _ in range(E):
    a, b = map(int, input().split())
    nodes[a].append(b)

def tarjan(path, V):
    label = [0]                 # 방문 순서 카운터
    labels = [0] * (V + 1)      # dfn(방문 순서)
    low = [0] * (V + 1)         # low-link
    onstack = [False] * (V + 1) # 현재 스택에 있는지
    s = []
    sccs = []

    def dfs(u):
        label[0] += 1
        labels[u] = low[u] = label[0]
        s.append(u)
        onstack[u] = True

        for v in path[u]:
            if labels[v] == 0:
                dfs(v)
                low[u] = min(low[u], low[v])
            elif onstack[v]:
                low[u] = min(low[u], labels[v])

        # SCC 루트면 스택에서 꺼내서 하나의 SCC 구성
        if low[u] == labels[u]:
            comp = []
            while True:
                p = s.pop()
                onstack[p] = False
                comp.append(p)
                if p == u:
                    break
            sccs.append(comp)

    for e in range(1, V + 1):
        if labels[e] == 0:
            dfs(e)

    return sccs

ans = tarjan(nodes, V)

# 문제 출력 조건: 각 SCC 내부 오름차순, SCC는 최소 원소 기준 오름차순
for comp in ans:
    comp.sort()
ans.sort(key=lambda x: x[0])

print(len(ans))
for comp in ans:
    print(*comp, -1)
