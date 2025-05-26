import sys
from collections import deque
input = sys.stdin.readline

N , K = map(int, input().split())

visited = [False] * 100001

def bfs(start, end):
    INF = 10 ** 9
    dist = [INF] * 100001
    dist[start] = 0
    dq = deque([start])

    while dq:
        x = dq.popleft()
        if x == end:
            break  # 이 지점에서 dist[end]가 최소

        # 순간이동
        nx = x * 2
        if 0 <= nx <= 100000 and dist[nx] > dist[x]:
            dist[nx] = dist[x]
            dq.appendleft(nx)

        # 앞으로/뒤로
        for nx in (x - 1, x + 1):
            if 0 <= nx <= 100000 and dist[nx] > dist[x] + 1:
                dist[nx] = dist[x] + 1
                dq.append(nx)

    print(dist[end])

bfs(N, K)
