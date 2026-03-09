N = int(input())

for i in range(N):
    M = int(input())

    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    dp = [[0] * 2 for _ in range(max(2, M + 1))]
    dp[0][0] = arr1[0]
    dp[0][1] = arr2[0]
    if M > 1:
        dp[1][0] = arr1[1] + arr2[0]
        dp[1][1] = arr2[1] + arr1[0]


    for j in range(2, M):
        dp[j][0] = max(dp[j - 1][1], dp[j - 2][1]) + arr1[j]
        dp[j][1] = max(dp[j - 1][0], dp[j - 2][0]) + arr2[j]

    print(max(dp[M-1][0], dp[M-1][1]))