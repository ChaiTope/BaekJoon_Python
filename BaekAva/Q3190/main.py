import sys
from collections import deque

input = sys.stdin.readline

N, K = int(input()), int(input())
board = [[0] * N for _ in range(N)]
res = 0

for i in range(K):
    x, y = map(int, input().split())

    board[x-1][y-1] = 1

L = int(input())
moves = [list(map(str, input().split())) for _ in range(L)]

queue = deque()
queue.append((0, 0))
board[0][0] = 2

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
d = 0

def move(i, j):
    global res
    res += 1

    if ((not (0 <= i < N and 0 <= j < N)) or
        board[i][j] == 2):
        print(res)
        sys.exit()

    apple = (board[i][j] == 1)

    if not apple:
        tx, ty = queue.popleft()
        board[tx][ty] = 0

    queue.append((i, j))
    board[i][j] = 2

x, y = queue[0]
prev = 0
for s, m in moves:
    for i in range(int(s) - prev):
        dx, dy = dirs[d]
        x, y = x + dx, y + dy
        move(x, y)

    if m == 'L':
        d = (d - 1) % 4

    else:
        d = (d + 1) % 4
    prev = int(s)

while True:
    dx, dy = dirs[d]
    x, y = x + dx, y + dy
    move(x, y)