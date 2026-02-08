import sys

input = sys.stdin.readline

N, M = map(int, input().split())

x, y, d = map(int, input().split())

# 0: 북, 1: 동, 2: 남, 3: 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

board = [list(map(int, input().split())) for _ in range(N)]

ans = 0

while True:
    # 1) 현재 칸 청소
    if board[x][y] == 0:
        board[x][y] = 2
        ans += 1

    moved = False

    # 2) 왼쪽부터 4방 탐색
    for _ in range(4):
        d = (d + 3) % 4  # 왼쪽 회전
        nx = x + dx[d]
        ny = y + dy[d]

        if board[nx][ny] == 0:   # 미청소 빈칸이면 전진
            x, y = nx, ny
            moved = True
            break

    if moved:
        continue

    # 3) 4방 다 없으면 후진
    back = (d + 2) % 4
    bx = x + dx[back]
    by = y + dy[back]

    if board[bx][by] == 1:  # 뒤가 벽이면 종료
        break

    x, y = bx, by  # 후진 (방향 d는 그대로)

print(ans)