import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M = map(int, input().split())

campus = [[""]*M for _ in range(N)]

dx, dy = 0, 0
mp = 0

for i in range(N):
    row = list(input().rstrip())
    for j in range(M):
        campus[i][j] = row[j]
        if row[j] == "I":
            dx = i
            dy = j

visited = [[False]*M for _ in range(N)]

def dfs(i, j):
    global mp
    if visited[i][j]:
        return

    visited[i][j] = True
    if campus[i][j] == "X":
        return
    if campus[i][j] == "P":
        mp += 1

    if i > 0:
        dfs(i-1, j)
    if j > 0:
        dfs(i, j-1)
    if j < M-1:
        dfs(i, j+1)
    if i < N-1:
        dfs(i+1, j)

dfs(dx, dy)
if mp == 0:
    print("TT")
else:
    print(mp)