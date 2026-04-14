## 보드에 가야하는 거리가 정해져있을 떄, 도착점까지의 최단시간

from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
dist = [[0] * N for _ in range(N)]
dirs = [(1, 0), (0, 1)]
queue = deque([(0, 0, board[0][0])])

while queue:
    x, y, j = queue.popleft()
    if x == N-1 and y == N-1:
        break

    for dx, dy in dirs:
        nx = x + (dx * j)
        ny = y + (dy * j)
        if nx < N and ny < N:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny, board[nx][ny]))

print(dist[N-1][N-1])
print(*dist, sep='\n')