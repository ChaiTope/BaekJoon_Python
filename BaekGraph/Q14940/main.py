import collections
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(N)]
p1, p2 = 0, 0

for i in range(N):
    for j in range(M):
        if maps[i][j] == 2:
            p1, p2 = i, j

dist = [[-1]*M for _ in range(N)]

dist[p1][p2] = 0

q = collections.deque([(p1, p2)])

while q:
    x, y = q.popleft()
    for dx, dy in ((-1,0),(1,0),(0,-1),(0,1)):
        nx, ny = x+dx, y+dy
        # 1) x,y 범위 확인
        if not (0 <= nx < N and 0 <= ny < M):
            continue
        # 2) 벽(0)인지, 이미 방문했는지 확인
        if maps[nx][ny] == 0 or dist[nx][ny] != -1:
            continue

        dist[nx][ny] = dist[x][y] + 1
        q.append((nx, ny))


# 출력
for i in range(N):
    for j in range(M):
        if maps[i][j] == 0:
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()