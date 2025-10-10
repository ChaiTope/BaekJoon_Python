import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))

l, r = 0, N - 1
best = 10**19
ans_l, ans_r = a[l], a[r]

while l < r:
    s = a[l] + a[r]
    if abs(s) < best:
        best = abs(s)
        ans_l, ans_r = a[l], a[r]
        if best == 0:
            break

    if s < 0:
        l += 1
    else:
        r -= 1

print(ans_l, ans_r)
