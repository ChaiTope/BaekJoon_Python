import sys
from sys import setrecursionlimit

setrecursionlimit(10 ** 6)

input = sys.stdin.readline

N = int(input())

in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

root = post_order[-1]

pos = [0] * (N + 1)

for i, v in enumerate(in_order):
    pos[v] = i

out = []

def solve(inL, inR, postL, postR):
    if inL > inR or postL > postR:
        return

    root = post_order[postR]
    out.append(root)

    K = pos[root]
    leftSize = K - inL

    solve(inL, K - 1, postL, postL + leftSize -1)
    solve(K + 1, inR, postL + leftSize, postR - 1)

solve(0, N-1, 0, N-1)
print(*out)