N = int(input())

dp = [0] * max(5,(N + 1))
dp[1] = 1
dp[3] = 1
for i in range(4, N + 1):
    if not dp[i-1] and not dp[i-3] and not dp[i-4]:
        dp[i] =1

if dp[N] != 0:
    print("CY")
else:
    print("SK")