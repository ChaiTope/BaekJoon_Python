import sys

input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))
dp = array[:]

for i in range(N):
    for j in range(i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + array[i])

print(max(dp))