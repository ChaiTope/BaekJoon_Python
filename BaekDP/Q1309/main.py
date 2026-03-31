N = int(input())
dp = [0] * (N + 1)
dp[0] = 1
dp[1] = 3
for i in range(2, N+1):
    dp[i] = 2 * dp[i - 1] + dp[i - 2]
print(dp[N])

a, b = 1, 3
for _ in range(2, N+1):
    a, b = b, (2*b + a) % 9901
print(b)