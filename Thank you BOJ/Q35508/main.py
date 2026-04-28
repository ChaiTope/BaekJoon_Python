import sys
from bisect import bisect_right

input = sys.stdin.readline

N, D = map(int, input().split())
# T, A, B (시간, 점수, 점수)
board = [list(map(int, input().split())) for _ in range(N)]
board.sort()
res = 0

# 최대값 갱신
prefix1 = [0]*N
prefix2 = [0]*N
time = [0]*N

prefix1[0] = board[0][1]
prefix2[0] = board[0][2]
time[0] = board[0][0]

for i in range(1, N):
    time[i] = board[i][0]
    prefix1[i] = max(prefix1[i-1], board[i][1])
    prefix2[i] = max(prefix2[i-1], board[i][2])

for i in range(N):
    rest = D - time[i]
    j = bisect_right(time, rest) - 1

    if j < 0:
        continue

    res = max(res, board[i][1] + prefix2[j])

print(res)