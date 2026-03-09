N = int(input())

dp = [0] * max(5,(N + 1))
dp[1] = 1
dp[3] = 1
dp[4] = 1
for i in range(5, N + 1):
    if dp[i-1] + dp[i-3] + dp[i-4] < 3:
        dp[i] =1
    else:
        dp[i] =0

if dp[N] != 0:
    print("SK")
else:
    print("CY")