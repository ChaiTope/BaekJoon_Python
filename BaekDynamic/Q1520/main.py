import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

M, N = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(M)]

dp = [[-1] * N for _ in range(M)]  # -1: 아직 계산 안 됨

dirs = [(1,0), (-1,0), (0,1), (0,-1)]

def dfs(x, y):
    # 1) 도착지면 경로 1개
    if x == M - 1 and y == N - 1:
        return 1

    # 2) 이미 계산한 적 있으면 그대로 사용
    if dp[x][y] != -1:
        return dp[x][y]

    # 3) 이제 이 칸의 답을 계산 시작 (0으로 초기화)
    dp[x][y] = 0
    cur = maps[x][y]

    # 4) 내리막으로만 이동하면서 합산
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < M and 0 <= ny < N:
            if maps[nx][ny] < cur:
                dp[x][y] += dfs(nx, ny)

    return dp[x][y]

print(dfs(0, 0))
