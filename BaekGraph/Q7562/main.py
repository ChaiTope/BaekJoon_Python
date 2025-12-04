import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
moves = [[1, 2], [2, 1], [-1, 2], [-2, 1], [-1, -2], [-2, -1], [1, -2], [2, -1]]

for i in range(T):
    l = int(input())
    sx, sy = list(map(int, input().split()))
    ex, ey = list(map(int, input().split()))
    dist = [[-1] * l for _ in range(l)]

    dist[sx][sy] = 0
    q = deque()
    q.append((sx, sy))

    while q:
        x, y = q.popleft()

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < l and 0 <= ny < l and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1

                q.append((nx, ny))
    print(dist[ex][ey])