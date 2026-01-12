import sys
input = sys.stdin.readline

A, B = map(int, input().split())

def ones_upto(n):
    if n < 0:
        return 0
    total = 0
    t = n + 1  # count of numbers: 0..n

    i = 0
    while (1 << i) <= n:
        half = 1 << i           # 2^i
        block = half << 1       # 2^(i+1)

        full = t // block
        rem  = t % block

        total += full * half + max(0, rem - half)
        i += 1

    return total

print(ones_upto(B) - ones_upto(A - 1))
