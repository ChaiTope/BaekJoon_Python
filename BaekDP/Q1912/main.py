N = int(input())

arr = list(map(int, input().split()))

dp = [0] * N

for i in range(N):
    dp[i] = max(arr[i], dp[i - 1] + arr[i])

print(max(dp))