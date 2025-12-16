import sys

input = sys.stdin.readline

N, M = map(int, input().split())
field = [input().rstrip() for _ in range(N)]

visited = [[False]*M for _ in range(N)]
done = [[False]*M for _ in range(N)]
cnt_cycle = 0

def nxt(x, y):
    d = field[x][y]
    if d == 'U': return x-1, y
    if d == 'D': return x+1, y
    if d == 'L': return x, y-1
    return x, y+1

for i in range(N):
    for j in range(M):
        if done[i][j]:
            continue

        path = []
        x, y = i, j

        while True:
            if done[x][y]:
                break

            if visited[x][y]:
                cnt_cycle += 1
                break

            visited[x][y] = True
            path.append((x, y))
            x, y = nxt(x, y)

        for px, py in path:
            done[px][py] = True

print(cnt_cycle)