import collections
import sys
input = sys.stdin.readline

T = int(input())

def is_bipartite(s, color):
    global check_bi

    queue = collections.deque()
    queue.append(s)
    colors[s] = color

    while queue and check_bi:
        v = queue.popleft()
        for w in graph[v]:
            if colors[w] == 0:
                colors[w] = -colors[v]
                queue.append(w)
            elif colors[w] == colors[v]:
                check_bi = False
                return

for _ in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    colors = [0] * (V + 1)   # 0=미방문, 1/-1=색
    check_bi = True

    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, V + 1):
        if not check_bi:
            break
        if colors[i] == 0:
            is_bipartite(i, 1)

    print("YES" if check_bi else "NO")