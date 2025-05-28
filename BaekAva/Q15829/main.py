import sys
input = sys.stdin.readline

N = int(input())
s = input().rstrip()

mod = 1234567891
res = 0
p = 1

for c in s:
    num = ord(c) - ord('a') + 1
    res = (res + num * p) % mod
    p = (p * 31) % mod

print(res)
