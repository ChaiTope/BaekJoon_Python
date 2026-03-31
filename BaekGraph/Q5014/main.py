import sys
from collections import deque

F, S, G, U, D = map(int, input().split())
visited = [-1] * F
visited[S-1] = 0

if S == G:
    print(0)
    sys.exit(0)

def bfs(start, end):
    queue = deque([start])

    while queue:
        v = queue.popleft()

        if v == end:
            print(visited[v])
            sys.exit(0)

        vu, vd = v + U, v - D

        if vu < F and visited[vu] == -1:
            queue.append(vu)
            visited[vu] = visited[v] + 1
        if vd >= 0 and visited[vd] == -1:
            queue.append(vd)
            visited[vd] = visited[v] + 1
    print("use the stairs")

bfs(S-1, G-1)