import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(input().rstrip()) for _ in range(N)]
DIRS = [(-1,0),(1,0),(0,-1),(0,1)]

def roll(board, x, y, dx, dy):
    # board[x][y]는 'R'/'B'가 있던 자리라고 가정 (호출 전에 '.'로 비워두고 굴리는 걸 추천)
    moved = 0
    while True:
        nx, ny = x + dx, y + dy
        cell = board[nx][ny]

        if cell == '#':      # 벽이면 멈춤
            return x, y, moved, False

        x, y = nx, ny
        moved += 1

        if cell == 'O':      # 구멍이면 빠짐
            return x, y, moved, True

def tilt(board, rx, ry, bx, by, dx, dy):
    # 2) 굴리기
    nrx, nry, rmove, r_hole = roll(board, rx, ry, dx, dy)
    nbx, nby, bmove, b_hole = roll(board, bx, by, dx, dy)

    # 3) 파란 구슬이 빠지면 실패
    if b_hole:
        # 보드 원복은 BFS에서 보드를 공유 안 하면 필요 없음. (복사/불변 설계 추천)
        return None  # "invalid move" 같은 의미로

    # 4) 둘 다 구멍 아닌데 같은 칸이면 겹침 해결
    if (not r_hole) and (nrx == nbx and nry == nby):
        if rmove > bmove:
            nrx -= dx
            nry -= dy
        else:
            nbx -= dx
            nby -= dy

    return nrx, nry, nbx, nby, r_hole

for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            rx, ry = i, j
            board[i][j] = '.'
        elif board[i][j] == 'B':
            bx, by = i, j
            board[i][j] = '.'

def bfs(rx, ry, bx, by):
    q = deque()
    q.append((rx, ry, bx, by, 0))
    visited = set()
    visited.add((rx, ry, bx, by))

    while q:
        rx, ry, bx, by, depth = q.popleft()

        if depth == 10:
            continue

        for dx, dy in DIRS:
            # ===== 여기서 tilt 호출 =====
            res = tilt(board, rx, ry, bx, by, dx, dy)

            # (A) tilt에서 "파란 빠지면 None" 방식
            if res is None:
                continue

            nrx, nry, nbx, nby, red_in_hole = res

            # 빨간만 빠짐 성공
            if red_in_hole:
                return depth + 1

            # 변화 없으면 스킵(옵션인데 넣는 거 추천)
            if (nrx, nry, nbx, nby) == (rx, ry, bx, by):
                continue

            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))
                q.append((nrx, nry, nbx, nby, depth + 1))

    return -1

print(bfs(rx, ry, bx, by))