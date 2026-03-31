import sys

input = sys.stdin.readline
N = int(input())
L = sorted(list(map(int, input().split())))
l, r = 0, N-1
res = float("inf")
lp, rp = L[0], L[-1]

while l < r:
    if L[l] + L[r] == 0:
        lp, rp = L[l], L[r]
        break

    if res > abs(L[l] + L[r]):
        lp = L[l]
        rp = L[r]
        res = abs(L[l] + L[r])

    if L[l] + L[r] > 0:
        r -= 1
    elif L[l] + L[r] < 0:
        l += 1

print(lp, rp)