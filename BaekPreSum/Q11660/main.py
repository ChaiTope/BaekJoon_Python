import sys

input = sys.stdin.readline

N, M = map(int, input().split())

nums = [[0]*(N+1) for _ in range(N+1)]
summary = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N + 1):
    index = list(map(int, input().split()))
    for j in range(1, N + 1):
        nums[i][j] = index[j-1]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        summary[i][j] = nums[i][j] + summary[i][j-1] +summary[i-1][j] - summary[i-1][j-1]

for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    res = summary[x2][y2]- summary[x1 - 1][y2]- summary[x2][y1 - 1]+ summary[x1 - 1][y1 - 1]
    print(res)
