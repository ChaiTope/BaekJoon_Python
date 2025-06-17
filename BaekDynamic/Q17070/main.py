import sys
input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# 올바른 3차원 DP 초기화
dp = [[[0, 0, 0] for _ in range(N)] for __ in range(N)]

# 초기 파이프 위치: (0,0)-(0,1) 가로 상태
dp[0][1][0] = 1

for i in range(N):
    for j in range(2, N):  # j=2부터 오른쪽·아래·대각 전이 검사
        if grid[i][j] == 0:
            # 수평(→) 전이: 왼쪽 칸이 비었어야
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][1]

        if i > 0 and grid[i][j] == 0 and grid[i-1][j] == 0 and grid[i][j-1] == 0:
            # 대각선(↘) 전이: 위·왼쪽·현재 모두 비어 있어야
            dp[i][j][1] = (dp[i-1][j-1][0] +
                           dp[i-1][j-1][1] +
                           dp[i-1][j-1][2])

        if i > 0 and grid[i][j] == 0:
            # 수직(↓) 전이: 위 칸이 비었어야
            dp[i][j][2] = dp[i-1][j][1] + dp[i-1][j][2]

# (N-1, N-1)에서 모든 방향 합을 출력
result = dp[N-1][N-1][0] + dp[N-1][N-1][1] + dp[N-1][N-1][2]
print(result)
