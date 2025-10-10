import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# 상, 좌, 우, 하 (타이브레이크 안전)
dirs = [(-1,0), (0,-1), (0,1), (1,0)]

# 상어 초기 상태 찾기
for i in range(N):
    for j in range(N):
        if grid[i][j] == 9:
            sx, sy = i, j
            grid[i][j] = 0   # 시작 위치를 빈칸으로 바꿔줌
            break

size = 2       # 상어 크기
eat = 0        # 지금까지 먹은 마릿수
time_sum = 0   # 총 시간

def bfs_pick_target(sx, sy, size):
    visited = [[False]*N for _ in range(N)]
    q = deque([(sx, sy, 0)])  # (x, y, dist)
    visited[sx][sy] = True

    candidates = []
    min_dist = None

    while q:
        x, y, d = q.popleft()

        # 이미 최소 거리보다 멀면 멈춤
        if min_dist is not None and d > min_dist:
            break

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if grid[nx][ny] <= size:  # 통과 가능
                    visited[nx][ny] = True
                    nd = d + 1
                    if 0 < grid[nx][ny] < size:  # 먹을 수 있음
                        candidates.append((nd, nx, ny))
                        if min_dist is None or nd < min_dist:
                            min_dist = nd
                    else:
                        q.append((nx, ny, nd))

    if not candidates:
        return None
    candidates.sort()  # (dist, x, y) 순 정렬
    return candidates[0]  # (dist, x, y)

while True:
    res = bfs_pick_target(sx, sy, size)
    if res is None:  # 더 이상 먹을 물고기 없음
        break

    dist, tx, ty = res
    time_sum += dist
    eat += 1
    sx, sy = tx, ty
    grid[tx][ty] = 0  # 먹은 자리 비워줌

    if eat == size:
        size += 1
        eat = 0

print(time_sum)