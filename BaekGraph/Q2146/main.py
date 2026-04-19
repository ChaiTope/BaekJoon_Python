from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
coasts = dict()

def labeling():
    island_id = 2

    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                q = deque([(i, j)])
                board[i][j] = island_id
                coasts[island_id] = []

                while q:
                    x, y = q.popleft()
                    is_coast = False

                    for dx, dy in dirs:
                        nx, ny = x + dx, y + dy

                        if 0 <= nx < N and 0 <= ny < N:
                            if board[nx][ny] == 1:
                                board[nx][ny] = island_id
                                q.append((nx, ny))
                            elif board[nx][ny] == 0:
                                is_coast = True

                    if is_coast:
                        coasts[island_id].append((x, y))

                island_id += 1

def bridge(start_id):
    visited = [[-1] * N for _ in range(N)]
    q = deque()

    for x, y in coasts[start_id]:
        q.append((x, y))
        visited[x][y] = 0

    while q:
        x, y = q.popleft()

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N:
                # 바다로 확장
                if board[nx][ny] == 0 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

                # 다른 섬 도착
                elif board[nx][ny] != 0 and board[nx][ny] != start_id:
                    return visited[x][y]

    return float('inf')

labeling()

answer = float('inf')
for island_id in coasts:
    answer = min(answer, bridge(island_id))

print(answer)