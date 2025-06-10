import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())
box = [[[0]*M for _ in range(N)] for __ in range(H)]
dq = deque()
# 1) 입력받으면서 익은 토마토(1)는 dq에 (z,y,x,day=0)로 넣기
for z in range(H):
    for y in range(N):
        row = list(map(int, input().split()))
        for x, v in enumerate(row):
            box[z][y][x] = v
            if v == 1:
                dq.append((z, y, x, 0))

dirs = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
max_day = 0

# 2) BFS
while dq:
    z, y, x, day = dq.popleft()
    max_day = max(max_day, day)
    for dz, dy, dx in dirs:
        nz, ny, nx = z+dz, y+dy, x+dx
        if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M and box[nz][ny][nx] == 0:
            box[nz][ny][nx] = 1
            dq.append((nz, ny, nx, day+1))

# 3) 다 돌고 나서 0(안 익은 토마토)이 남아 있으면 -1, 아니면 max_day 출력
for z in range(H):
    for y in range(N):
        if 0 in box[z][y]:
            print(-1)
            sys.exit(0)
print(max_day)
