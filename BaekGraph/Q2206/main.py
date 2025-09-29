import sys
from collections import deque

input = sys.stdin.readline

# 입력/초기화 예시
N, M = map(int, input().split())
K = 1# 행, 열, 최대 부술 수
grid = [list(map(int, input().strip())) for _ in range(N)]     # N x M 0/1 맵 (0=빈칸, 1=벽)

# 방문: visited[x][y][k] => (x,y)에 벽 k개 부수고 최초 도달했는가
visited = [[[False]*(K+1) for _ in range(M)] for __ in range(N)]

# BFS: (x, y, broken, dist)
q = deque()
q.append((0, 0, 0, 1))  # 시작을 거리 1로 할지 0으로 할지는 문제 정의에 맞춰 조정
visited[0][0][0] = True

dirs = [(1,0), (-1,0), (0,1), (0,-1)]

ans = -1
while q:
    x, y, broken, dist = q.popleft()

    # 목표 도달 체크 (문제에 맞게 좌표 수정)
    if x == N-1 and y == M-1:
        ans = dist
        break

    for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        if not (0 <= nx < N and 0 <= ny < M):
            continue

        # 빈 칸이면 그냥 이동 (벽 추가로 안 부숨)
        if grid[nx][ny] == 0:
            if not visited[nx][ny][broken]:
                visited[nx][ny][broken] = True
                q.append((nx, ny, broken, dist+1))

        # 벽이면, 아직 부술 기회 남았을 때만 부수고 이동
        else:  # grid[nx][ny] == 1
            if broken < K and not visited[nx][ny][broken+1]:
                visited[nx][ny][broken+1] = True
                q.append((nx, ny, broken+1, dist+1))

print(ans)  # 도달 불가면 -1