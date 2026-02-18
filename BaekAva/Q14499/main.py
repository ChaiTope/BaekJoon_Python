import sys

input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

# 동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
cmds = list(map(int, input().split()))

dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]

dice = [0] * 6

for d in cmds:
    dx, dy = dirs[d-1]

    nx = x + dx
    ny = y + dy

    if 0 <= nx < N and 0 <= ny < M:
        tmp = dice[:]

        if d == 1:  # 동
            dice[0] = tmp[4]
            dice[1] = tmp[5]
            dice[5] = tmp[0]
            dice[4] = tmp[1]
            dice[2] = tmp[2]
            dice[3] = tmp[3]
        elif d == 2:  # 서
            dice[0] = tmp[5]
            dice[1] = tmp[4]
            dice[5] = tmp[1]
            dice[4] = tmp[0]
            dice[2] = tmp[2]
            dice[3] = tmp[3]
        elif d == 3:  # 북
            dice[0] = tmp[3]
            dice[1] = tmp[2]
            dice[2] = tmp[0]
            dice[3] = tmp[1]
            dice[4] = tmp[4]
            dice[5] = tmp[5]
        else:  # 남
            dice[0] = tmp[2]
            dice[1] = tmp[3]
            dice[2] = tmp[1]
            dice[3] = tmp[0]
            dice[4] = tmp[4]
            dice[5] = tmp[5]

        x, y = nx, ny

        if board[x][y] == 0:
            board[x][y] = dice[1]
        else:
            dice[1] = board[x][y]
            board[x][y] = 0

        print(dice[0])