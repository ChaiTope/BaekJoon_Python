from collections import deque

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
res = 0

def bfs(start):
    global res
    visited = [[-1] * M for _ in range(N)]
    queue = deque([start])
    visited[start[0]][start[1]] = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == "L":
                    if visited[nx][ny] == -1:
                        visited[nx][ny] = visited[x][y] + 1
                        queue.append((nx, ny))

    res = max(res, max(map(max, visited)))

for i in range(N):
    for j in range(M):
        if board[i][j] == "L":
            bfs((i, j))

print(res)