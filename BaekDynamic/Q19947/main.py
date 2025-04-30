money, year = map(int, input().split())

dp = [0] * (year + 1)
dp[0] = money

for i in range(1, year+1):
    if i >= 5:
        dp[i] = max(dp[i], int(dp[i-5]*1.35))
    if i >= 3:
        dp[i] = max(dp[i] , int(dp[i-3]*1.2))
    else:
        dp[i] = int(dp[i-1]*1.05)

print(int(max(dp[year-1]*1.05, dp[year])))