import sys

input = sys.stdin.readline

R, C, M = map(int, input().split())

board = {}
directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
answer = 0

def fishhook(p):
    global answer
    for row in range(R):
        if (row, p) in board:
            answer += board[(row, p)][2]
            del board[(row, p)]
            break

def move():
    new_board = {}

    for (r, c), (s, d, z) in board.items():

        # 1) 세로/가로 판별(상어마다!)
        is_vertical = (d == 1 or d == 2)

        if is_vertical:
            L = R
            pos = r
            if R == 1:
                k = 0
                p = 0
            else:
                p = 2 * (R - 1)
                k = s % p
        else:
            L = C
            pos = c
            if C == 1:
                k = 0
                p = 0
            else:
                p = 2 * (C - 1)
                k = s % p

        # 2) p==0이면 이동 없음(제자리)
        if p == 0:
            nr, nc, nd = r, c, d

        else:
            # 3) 부호(dir_sign) 결정
            # 위(1), 왼(4) = -1 / 아래(2), 오른(3) = +1
            dir_sign = -1 if (d == 1 or d == 4) else 1

            # 4) 왕복 계산
            t = (pos + dir_sign * k) % p

            if t <= L - 1:
                new_pos = t
                new_dir_sign = dir_sign
            else:
                new_pos = p - t
                new_dir_sign = -dir_sign

            # 5) 좌표 복원 + 방향(nd) 재매핑
            if is_vertical:
                nr, nc = new_pos, c
                nd = 1 if new_dir_sign == -1 else 2
            else:
                nr, nc = r, new_pos
                nd = 3 if new_dir_sign == 1 else 4

        # 6) 충돌 처리: 같은 칸이면 큰 상어만
        if (nr, nc) not in new_board or new_board[(nr, nc)][2] < z:
            new_board[(nr, nc)] = (s, nd, z)

    return new_board

for i in range(M):
    r, c, s, d, z = map(int, input().split())

    board[(r-1,c-1)] = (s, d, z)

for col in range(C):
    fishhook(col)
    board = move()

print(answer)