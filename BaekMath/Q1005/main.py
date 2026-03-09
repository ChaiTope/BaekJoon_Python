import sys

N = int(input())
res = 99

if N < 100:
    print(N)
    sys.exit()

for i in range(100, N+1):
    a = i // 100
    b = i // 10 % 10
    c = i % 10

    if (b - a) == (c - b):
        res += 1

print(res)