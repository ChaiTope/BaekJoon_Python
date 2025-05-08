import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

ps = [0] * (N+1)
for i in range(N):
    ps[i+1] = ps[i] + arr[i]

#    (1-indexed 쿼리 기준)
for _ in range(M):
    l, r = map(int, input().split())
    print(ps[r] - ps[l-1])
