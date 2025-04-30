N = int(input())

nums = [float(input()) for _ in range(N)]
dp = nums[:]      # dp[i] = i에서 끝나는 구간의 최대 곱
ans = dp[0]

for i in range(1, N):
    # 새로 시작할지, 이전에 이어 붙일지 비교
    dp[i] = max(nums[i], dp[i-1] * nums[i])
    ans = max(ans, dp[i])

print(f"{ans:.3f}")
