import sys

sys.setrecursionlimit(300000)
input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
cnt = 0
res = []

def dfs(i, j):
    global d
    if board[i][j] == 0:
        return

    board[i][j] = 0
    d += 1

    for dx, dy in dirs:
        ni, nj = i + dx, j + dy
        if 0 <= ni < N and 0 <= nj < M:
            dfs(ni, nj)

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            d = 0
            dfs(i, j)
            cnt += 1
            res.append(d)

print(cnt)
print(max(res, default=0))