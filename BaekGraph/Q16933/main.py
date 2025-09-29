import sys
from collections import deque

input = sys.stdin.readline

N, M, K = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(N)]

INF = 10**9
# visited_min[x][y][p] = (x,y)에 낮/밤 p(1=낮, 0=밤)으로 도달할 때 사용한 최소 '부순 벽' 개수
visited_min = [[[INF, INF] for _ in range(M)] for __ in range(N)]

q = deque()
start_dist = 1  # 시작을 낮으로 간주 (문제 규칙에 맞춤)
visited_min[0][0][1] = 0
q.append((0, 0, 0, start_dist))  # (x, y, broken, dist)

dirs = ((1,0), (-1,0), (0,1), (0,-1))

ans = -1
while q:
    x, y, broken, dist = q.popleft()
    p = dist & 1  # 1=낮, 0=밤

    # 더 좋은(적게 부숨) 상태가 이미 기록되어 있으면 스킵
    if broken > visited_min[x][y][p]:
        continue

    if x == N - 1 and y == M - 1:
        ans = dist
        break

    nd = dist + 1
    np = nd & 1

    # 4방향 이동
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < N and 0 <= ny < M):
            continue

        if grid[nx][ny] == 0:
            # 빈칸은 언제나 이동 가능
            if broken < visited_min[nx][ny][np]:
                visited_min[nx][ny][np] = broken
                q.append((nx, ny, broken, nd))
        else:
            # 벽: 낮에만 부수고 이동 가능
            if p == 1 and broken < K:
                nb = broken + 1
                if nb < visited_min[nx][ny][np]:
                    visited_min[nx][ny][np] = nb
                    q.append((nx, ny, nb, nd))

    # ★ 조건부 '대기': 밤이고, 옆에 '벽'이 최소 하나 있고, 아직 부술 여지가 있을 때만
    if p == 0 and broken < K:
        need_wait = False
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 1:
                need_wait = True
                break
        if need_wait and broken < visited_min[x][y][np]:
            visited_min[x][y][np] = broken
            q.append((x, y, broken, nd))

print(ans)
