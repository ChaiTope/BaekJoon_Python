import sys

input = sys.stdin.readline

N = int(input())

liquids = sorted(list(map(int, input().split())))

res, ans_l, ans_r, ans_c = 10 ** 19, 10 ** 19, 10 ** 19, 10 ** 19

def two_pointer(l, r, c):
    global res, ans_l, ans_r, ans_c, N

    while l < r:
        s = liquids[l] + liquids[r] + liquids[c]
        if abs(s) < res:
            res = abs(s)
            ans_l, ans_r, ans_c = liquids[l], liquids[r], liquids[c]
            if res == 0:
                break

        if s < 0:
            l += 1
        else:
            r -= 1

for i in range(N - 2):
    n, m = i+1, N-1
    two_pointer(n, m, i)

print(ans_c, ans_l, ans_r)