import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def mod_pow(a, b, mod):
    if b == 0:
        return 1
    half = mod_pow(a, b // 2, mod)
    res = (half * half) % mod
    if b % 2:    # b가 홀수면 a 하나 더 곱해주기
        res = (res * a) % mod
    return res

print(mod_pow(A, B, C))