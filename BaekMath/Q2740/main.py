import sys

input = sys.stdin.readline

N, M = map(int, input().split())

f_list = [list(map(int, input().split())) for _ in range(N)]

M, K = map(int, input().split())

s_list = [list(map(int, input().split())) for _ in range(M)]

r_list = [[0]*K for _ in range(N)]

for i in range(N):
    for j in range(K):
        for k in range(M):
            r_list[i][j] = r_list[i][j] + f_list[i][k] * s_list[k][j]

for i in range(N):
    print(*r_list[i])