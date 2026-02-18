import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
dec = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

res = 0

def set_visited():
    global ice_cnt
    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                visited[i][j] = True
            else:
                ice_cnt += 1
                visited[i][j] = False

def dfs(x, y):
    visited[x][y] = True
    melt(x, y)

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny]:
                dfs(nx, ny)

def melt(i, j):
    count = 0
    for dx, dy in dirs:
        ni, nj = i + dx, j + dy

        if 0 <= ni < N and 0 <= nj < M:
            if board[ni][nj] == 0:
                count += 1

    dec[i][j] = count

while True:
    components = 0
    ice_cnt = 0
    set_visited()

    if ice_cnt == 0:
        print(0)
        break

    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                components += 1

                if components > 1:
                    print(res)
                    sys.exit(0)

                dfs(i, j)

    for i in range(N):
        for j in range(M):
            if board[i][j] > 0: board[i][j] = max(0, board[i][j] - dec[i][j])

    res += 1