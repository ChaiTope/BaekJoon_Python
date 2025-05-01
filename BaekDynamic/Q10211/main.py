N = int(input())

for i in range(N):
    n = int(input())
    nums = list(map(int, input().split()))
    dp = nums[:]
    ans = dp[0]

    for j in range(1, n):
        dp[j] = max(nums[j], dp[j - 1] + nums[j])
        ans = max(ans, dp[j])

    print(ans)