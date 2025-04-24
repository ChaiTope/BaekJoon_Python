N = int(input())

cost = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*3 for _ in range(N)]

prev = cost[0]
for i in range(1, N):
    curr = [0]*3
    curr[0] = cost[i][0] + min(prev[1], prev[2])
    curr[1] = cost[i][1] + min(prev[0], prev[2])
    curr[2] = cost[i][2] + min(prev[0], prev[1])
    prev = curr

print(min(prev))
