import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(N)]

visited = [[False]*M for _ in range(N)]
dist = [[0]*M for _ in range(N)]
Q = deque()

# 출발점 (0,0) 세팅
Q.append((0,0))
visited[0][0] = True
dist[0][0] = 1   # 1부터 시작(칸 수를 1로 셈)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

while Q:
    x, y = Q.popleft()

    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]

        # 경계 검사와 미방문, 길 여부 확인
        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny] and maze[nx][ny] == 1:
                visited[nx][ny] = True
                dist[nx][ny] = dist[x][y] + 1
                Q.append((nx, ny))

print(dist[N-1][M-1])  # (N-1, M-1)에 처음 도착했을 때 dist값이 최단 칸 수
