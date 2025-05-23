from collections import deque
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
boxes = [list(map(int, input().split())) for _ in range(M)]

q = deque()
dist = [[-1]*N for _ in range(M)]
# 1인 칸은 dist=0, 큐에 삽입
for i in range(M):
    for j in range(N):
        if boxes[i][j] == 1:
            dist[i][j] = 0
            q.append((i, j))

dirs = [(-1,0),(1,0),(0,-1),(0,1)]
max_day = 0

while q:
    x, y = q.popleft()
    for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        if 0 <= nx < M and 0 <= ny < N and boxes[nx][ny] == 0:
            boxes[nx][ny] = 1
            dist[nx][ny] = dist[x][y] + 1
            max_day = max(max_day, dist[nx][ny])
            q.append((nx, ny))
min_val = min(dist)

for row in boxes:
    if 0 in row:
        print(-1)
        break
else:
    print(max_day)