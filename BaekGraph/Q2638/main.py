import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

dirs = [(1,0), (-1,0), (0,1), (0,-1)]

def bfs_mark_and_touch():
    # 라운드용 visited/contact 초기화
    visited = [[False]*M for _ in range(N)]
    contact = [[0]*M for _ in range(N)]
    q = deque([(0, 0)])
    visited[0][0] = True

    touched = set()  # 이번 라운드에 공기와 닿은 치즈 좌표 모음

    while q:
        x, y = q.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < M):
                continue

            if grid[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
            elif grid[nx][ny] == 1:
                # 외부 공기 한 면 접촉
                contact[nx][ny] += 1
                touched.add((nx, ny))
    return contact, touched

ans = 0
while True:
    contact, touched = bfs_mark_and_touch()

    melted = 0
    # BFS 끝난 뒤에 일괄로 녹이기 (동시성 보장)
    for x, y in touched:
        if contact[x][y] >= 2:
            grid[x][y] = 0
            melted += 1

    if melted == 0:
        break
    ans += 1

print(ans)
