import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상우하좌

cctvs = []
for i in range(N):
    for j in range(M):
        if 1 <= board[i][j] < 6:
            cctvs.append((board[i][j], i, j))

# CCTV 타입별 방향 옵션(각 옵션은 "감시할 방향 인덱스 리스트")
options = {
    1: [[0], [1], [2], [3]],
    2: [[0, 2], [1, 3]],
    3: [[0, 1], [1, 2], [2, 3], [3, 0]],
    4: [[0, 1, 3], [0, 1, 2], [1, 2, 3], [0, 2, 3]],
    5: [[0, 1, 2, 3]],
}

def watch(x, y, opt):
    changed = []
    for d in opt:
        dx, dy = dirs[d]
        nx, ny = x + dx, y + dy
        while 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] == 6:
                break
            if board[nx][ny] == 0:
                board[nx][ny] = -1
                changed.append((nx, ny))
            nx += dx
            ny += dy
    return changed

ans = 10**9

def dfs(idx):
    global ans
    if idx == len(cctvs):
        cnt = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] == 0:
                    cnt += 1
        if cnt < ans:
            ans = cnt
        return

    t, x, y = cctvs[idx]
    for opt in options[t]:
        changed = watch(x, y, opt)
        dfs(idx + 1)
        for a, b in changed:
            board[a][b] = 0

dfs(0)
print(ans)