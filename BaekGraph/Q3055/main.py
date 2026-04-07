import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
board = []
flood = []
water = [[-1 for _ in range(M)] for _ in range(N)]
dist = [[-1 for _ in range(M)] for _ in range(N)]

for i in range(N):
    line = list(input().strip())
    for j in range(M):
        if line[j] == "*":
            water[i][j] = 0
            flood.append((i, j))
        elif line[j] == "D":
            end = (i, j)
        elif line[j] == "S":
            start = (i, j)
    board.append(line)

dist[start[0]][start[1]] = 0

def water_bfs(path):
    queue = deque(path)

    while queue:
        r, c = queue.popleft()

        for dx, dy in dirs:
            nr, nc = r + dx, c + dy
            if 0 <= nr < N and 0 <= nc < M:
                if board[nr][nc] in ('.', 'S') and water[nr][nc] == -1:
                    queue.append((nr, nc))
                    water[nr][nc] = water[r][c] + 1

def bfs(start):
    queue = deque([start])
    while queue:
        r, c = queue.popleft()

        for dx, dy in dirs:
            nr, nc = r + dx, c + dy
            nt = dist[r][c] + 1
            if 0 <= nr < N and 0 <= nc < M and dist[nr][nc] == -1:
                if board[nr][nc] == "." and (water[nr][nc] == -1 or nt < water[nr][nc]):
                    queue.append((nr, nc))
                    dist[nr][nc] = nt
                elif board[nr][nc] == "D":
                    dist[nr][nc] = nt
                    return

water_bfs(flood)
bfs(start)

if dist[end[0]][end[1]] != -1:
    print(dist[end[0]][end[1]])
else:
    print("KAKTUS")