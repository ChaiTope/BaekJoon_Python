import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def tuck(graph, row, col):
    new_col, new_row = col + 2, row + 2
    padded = [[0] * new_col for _ in range(new_row)]

    for i in range(N):
        for j in range(M):
            padded[i+1][j+1] = graph[i][j]

    return padded

new_board = tuck(board, N, M)

def bfs():
    visited = [[False] * (M+2) for _ in range(N+2)]
    contact = [[0] * (M+2) for _ in range(N+2)]
    q = deque([(0, 0)])
    visited[0][0] = True

    touched = set()

    while q:
        x, y = q.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N+2 and 0 <= ny < M+2):
                continue

            if new_board[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))

            elif new_board[nx][ny] == 1:
                contact[nx][ny] += 1
                touched.add((nx, ny))

    return contact, touched

times, cheeses = 0, 0

while True:
    contact, touched = bfs()

    melted = 0

    for x, y in touched:
        if contact[x][y] >= 1:
            new_board[x][y] = 0
            melted += 1

    if melted == 0:
        break
    cheeses = melted
    times += 1

print(times)
print(cheeses)