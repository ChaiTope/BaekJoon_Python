import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
inc_dp = [1] * N
dec_dp = [1] * N

for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]:
            inc_dp[i] = max(inc_dp[i], inc_dp[j] + 1)

for i in range(N-1, -1, -1):
    for j in range(i+1, N):
        if arr[j] < arr[i]:
            dec_dp[i] = max(dec_dp[i], dec_dp[j] + 1)

answer = max(inc_dp[i] + dec_dp[i] - 1 for i in range(N))
print(answer)
