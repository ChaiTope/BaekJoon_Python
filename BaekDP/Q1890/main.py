N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N-1 and j == N-1:
            continue
        n = board[i][j]
        ni, nj = n + i, n + j
        if ni < N:
            dp[ni][j] += dp[i][j]
        if nj < N:
            dp[i][nj] += dp[i][j]
print(dp[N-1][N-1])
print(*dp, sep='\n')