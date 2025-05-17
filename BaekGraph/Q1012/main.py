import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(i, j):
    if field[i][j] == 1:
        field[i][j] = 0
        if i > 0:
            dfs(i-1, j)
        if j > 0:
            dfs(i, j-1)
        if i < M-1:
            dfs(i+1, j)
        if j < N-1:
            dfs(i, j+1)

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())

    count = 0

    field = [[0] * N for _ in range(M)]

    for i in range(K):
        x, y = map(int, input().split())
        field[x][y] = 1

    for i in range(M):
        for j in range(N):
            if field[i][j] == 1:
                dfs(i, j)
                count += 1

    print(count)