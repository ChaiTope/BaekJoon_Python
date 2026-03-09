import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)
M, N, K = map(int, input().split())

board = [[0] * (N) for _ in range(M)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
cnt = 1
areas = []

def find(a, b):
    global area
    if board[a][b] != 0:
        return
    board[a][b] = cnt
    area += 1

    for d in dirs:
        x = a + d[0]
        y = b + d[1]
        if 0 <= x < M and 0 <= y < N:
            find(x, y)


for i in range(K):
    a, b, c, d = map(int, input().split())
    for y in range(b, d):
        for x in range(a, c):
            board[y][x] = -1

for i in range(M):
    for j in range(N):
        if board[i][j] == 0:
            area = 0
            find(i, j)
            cnt += 1
            areas.append(area)

print(cnt-1)
print(*sorted(areas))