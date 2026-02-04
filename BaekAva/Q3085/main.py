import sys

input = sys.stdin.readline

N = int(input())

board = [list(input().rstrip()) for _ in range(N)]

def check(board, N):
    best = 1

    # 가로 체크
    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if board[i][j] == board[i][j-1]:
                cnt += 1
            else:
                best = max(best, cnt)
                cnt = 1
        best = max(best, cnt)

    # 세로 체크
    for j in range(N):
        cnt = 1
        for i in range(1, N):
            if board[i][j] == board[i-1][j]:
                cnt += 1
            else:
                best = max(best, cnt)
                cnt = 1
        best = max(best, cnt)

    return best


def swap(board, x1, y1, x2, y2):
    board[x1][y1], board[x2][y2] = board[x2][y2], board[x1][y1]

dirs = [(-1,0), (1,0), (0,-1), (0,1)]

ans = check(board, N)

for i in range(N):
    for j in range(N):
        for dx, dy in dirs:
            ni, nj = i + dx, j + dy
            if 0 <= ni < N and 0 <= nj < N:
                if board[i][j] == board[ni][nj]:
                    continue

                swap(board, i, j, ni, nj)
                ans = max(ans, check(board, N))
                swap(board, i, j, ni, nj)  # 원복

print(ans)