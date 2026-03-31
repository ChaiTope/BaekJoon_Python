N = int(input())
if N % 2 == 1:
    print(0)

else:
    dp = [0] * (max(N + 1, 5))
    dp[0] = 1
    dp[2] = 3

    if N <= 2:
        print(dp[N])
    else:
        for i in range(4, N + 1, 2):
            dp[i] = 4 * dp[i - 2] - dp[i - 4]

        print(dp[N])