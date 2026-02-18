import sys
from sys import setrecursionlimit

setrecursionlimit(10**6)

input = sys.stdin.readline

N, L, R = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
res = 0

def dfs(x, y, path):
    visited[x][y] = True

    path.append((x, y))

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < N:
            if L <= abs(board[x][y] - board[nx][ny]) <= R:
                if not visited[nx][ny]:
                    dfs(nx, ny, path)


while True:
    visited = [[False] * N for _ in range(N)]
    moved = False

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                union = []
                dfs(i, j, union)

                if len(union) >= 2:
                    moved = True
                    total = 0

                    for x, y in union:
                        total += board[x][y]

                    avg = total // len(union)

                    for x, y in union:
                        board[x][y] = avg

                    moved = True

    if not moved:
        print(res)
        break
    res += 1