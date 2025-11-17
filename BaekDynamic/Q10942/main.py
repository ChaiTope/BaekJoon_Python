import sys
input = sys.stdin.readline

N = int(input())
arr = [0] + list(map(int, input().split()))

dp = [[0]*(N+1) for _ in range(N+1)]

# 길이 1
for i in range(1, N+1):
    dp[i][i] = 1

# 길이 2
for i in range(1, N):
    if arr[i] == arr[i+1]:
        dp[i][i+1] = 1

# 길이 3 이상
for length in range(3, N+1):
    for s in range(1, N-length+2):
        e = s + length - 1
        if arr[s] == arr[e] and dp[s+1][e-1] == 1:
            dp[s][e] = 1

M = int(input())
for _ in range(M):
    s, e = map(int, input().split())
    print(dp[s][e])
