import sys
input = sys.stdin.readline

n = int(input())
# dp[i] = i를 제곱수 합으로 표현할 때 필요한 최소 개수
dp = [0] + [10**9] * n

for i in range(1, n+1):
    # 1부터 sqrt(i)까지 모든 제곱수 j*j를 시도
    for j in range(1, int(i**0.5) + 1):
        dp[i] = min(dp[i], dp[i - j*j] + 1)

print(dp[n])
