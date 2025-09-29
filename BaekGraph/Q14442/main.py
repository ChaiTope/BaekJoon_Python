import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(N)]

visited = [[[False]*(K+1) for _ in range(M)] for __ in range(N)]

q = deque()
q.append((0, 0, 0, 1))
visited[0][0][0] = True

dirs = [(1,0), (-1,0), (0,1), (0,-1)]

ans = -1
while q:
    x, y, broken, dist = q.popleft()

    if x == N-1 and y == M-1:
        ans = dist
        break

    for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        if not (0 <= nx < N and 0 <= ny < M):
            continue

        if grid[nx][ny] == 0:
            if not visited[nx][ny][broken]:
                visited[nx][ny][broken] = True
                q.append((nx, ny, broken, dist+1))

        else:
            if broken < K and not visited[nx][ny][broken+1]:
                visited[nx][ny][broken+1] = True
                q.append((nx, ny, broken+1, dist+1))

print(ans)