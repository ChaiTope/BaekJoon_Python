import sys

input = sys.stdin.readline

N, M = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(N)]

K = int(input())

for _ in range(K):
    res = 0
    i, j, x, y = map(int, input().split())
    for a in range(i-1, x):
        for b in range(j-1, y):
            res += array[a][b]

    print(res)