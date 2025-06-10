import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())

rgb = [['']*N for i in range(N)]

rb = [['']*N for i in range(N)]

for i in range(N):
    colors = input().rstrip()

    for j in range(N):
        if colors[j] == 'G':
            rb[i][j] = 'R'
            rgb[i][j] = colors[j]
        else:
            rb[i][j] = colors[j]
            rgb[i][j] = colors[j]

visited_rgb = [[False]*N for i in range(N)]
visited_rb = [[False]*N for i in range(N)]
area_rgb = 0
area_rb = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def judge(x, y ,color, path, visited):
    if visited[x][y] or path[x][y] != color:
        return

    visited[x][y] = True

    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]

        if 0 <= nx < N and 0 <= ny < N:
            judge(nx, ny, color, path, visited)

for i in range(N):
    for j in range(N):
        if not visited_rgb[i][j]:
            judge(i,j, rgb[i][j], rgb, visited_rgb)
            area_rgb += 1

        if not visited_rb[i][j]:
            judge(i,j, rb[i][j], rb, visited_rb)
            area_rb += 1


print(area_rgb)
print(area_rb)