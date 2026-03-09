N = int(input())

score = [int(input()) for i in range(N)]
dp = [[0] * 3 for j in range(N)]

# 0번 계단
dp[0][1] = score[0]

if N > 1:
    # 1번 계단
    dp[1][1] = score[1]
    dp[1][2] = score[0] + score[1]

for i in range(2, N):
    dp[i][1] = max(dp[i - 2][1], dp[i - 2][2]) + score[i]
    dp[i][2] = dp[i - 1][1] + score[i]

print(max(dp[N-1][1], dp[N-1][2]))