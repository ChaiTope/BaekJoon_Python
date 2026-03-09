N = int(input())

for i in range(N):
    n = int(input())

    dp = [0] * max(2, (n + 1))
    dp[0] = 0
    dp[1] = 1


    if n == 0:
        print(1, 0)
    else:
        for j in range(2, n + 1):
            dp[j] = dp[j - 1] + dp[j - 2]
        print(dp[n-1], dp[n])