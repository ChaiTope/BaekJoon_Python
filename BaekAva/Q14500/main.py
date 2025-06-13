import sys

input = sys.stdin.readline

N, M = map(int, input().split())
max_val = 0
paper = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * M for _ in range(N)]

def tetris(x, y, summary, length):
    global max_val
    if length == 4:
        max_val = max(max_val, summary)
        return

    for dir in range(4):
        nx, ny = x + dx[dir], y + dy[dir]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            tetris(nx, ny, summary + paper[nx][ny], length + 1)
            visited[nx][ny] = False


def check_fu(x, y):
    global max_val

    wings = []
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < N and 0 <= ny < M:
            wings.append(paper[nx][ny])

    if len(wings) == 3:
        # 모서리인 경우: 있는 3칸 전부 더하기
        total = paper[x][y] + sum(wings)
        max_val = max(max_val, total)
    elif len(wings) == 4:
        # 중앙인 경우: 네 칸 중 가장 작은 날개 하나 빼고 더하기
        total = paper[x][y] + sum(wings) - min(wings)
        max_val = max(max_val, total)

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        tetris(i, j, paper[i][j], 1)
        visited[i][j] = False

        check_fu(i, j)

print(max_val)