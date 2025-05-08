import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

ps = [0] * (N+1)
for i in range(N):
    ps[i+1] = ps[i] + arr[i]

max_sum = -10**9
for i in range(N - M + 1):
    max_sum = max(max_sum, ps[i+M] - ps[i])

print(max_sum)
