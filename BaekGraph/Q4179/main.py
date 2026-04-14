import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
board = []
flood = []
fire = [[-1] * M for _ in range(N)]
dist = [[-1] * M for _ in range(N)]

for i in range(N):
    line = list(input().strip())
    for j in range(M):
        if line[j] == "F":
            fire[i][j] = 0
            flood.append((i, j))
        elif line[j] == "J":
            start = (i, j)
    board.append(line)

dist[start[0]][start[1]] = 0

def fire_bfs():
    queue = deque(flood)
    while queue:
        r, c = queue.popleft()
        for dx, dy in dirs:
            nr, nc = r + dx, c + dy
            if 0 <= nr < N and 0 <= nc < M:
                if board[nr][nc] != '#' and fire[nr][nc] == -1:
                    fire[nr][nc] = fire[r][c] + 1
                    queue.append((nr, nc))

def bfs():
    queue = deque([start])
    while queue:
        r, c = queue.popleft()
        for dx, dy in dirs:
            nr, nc = r + dx, c + dy
            nt = dist[r][c] + 1

            if not (0 <= nr < N and 0 <= nc < M):
                return nt

            if dist[nr][nc] == -1 and board[nr][nc] == '.':
                if fire[nr][nc] == -1 or nt < fire[nr][nc]:
                    dist[nr][nc] = nt
                    queue.append((nr, nc))
    return 0

fire_bfs()
res = bfs()
print(res if res else "IMPOSSIBLE")