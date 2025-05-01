N = int(input())

dp = [0] * max(N + 1, 4)
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 5

for i in range(4, N + 1):
    for j in range(i):
        dp[i] += dp[j] * dp[i-j-1]

print(dp[N])
