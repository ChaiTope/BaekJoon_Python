import sys
from collections import deque

input = sys.stdin.readline

d = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),          (0, 1),
    (1, -1),  (1, 0), (1, 1)
]

def bfs(si, sj):
    q = deque()
    q.append((si, sj))
    visited[si][sj] = True

    while q:
        a, b = q.popleft()

        for dx, dy in d:
            na, nb = a + dx, b + dy

            if 0 <= na < h and 0 <= nb < w:
                if not visited[na][nb] and board[na][nb] == 1:
                    visited[na][nb] = True
                    q.append((na, nb))

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    board = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if board[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                cnt += 1

    print(cnt)