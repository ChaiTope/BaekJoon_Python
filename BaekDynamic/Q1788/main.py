import sys

input = sys.stdin.readline

N = int(input())

a, b, c = 0, 1, 0

if N == 1:
    print(1)
    print(1)
elif N == 0:
    print(0)
    print(0)
elif N == -1:
    print(1)
    print(1)
else:
    if N < 0 :
        N = abs(N)
        for i in range(1, N):
            if a - b < 0 :
                c = 0 - (abs(a - b) % 1000000000)
            else:
                c = (a - b) % 1000000000
            a, b = b, c
    else:
        for i in range(1, N):
            c = (a + b) % 1000000000
            a, b = b, c

    if c < 0:
        print(-1)
        print(abs(c))
    elif c == 0:
        print(0)
        print(0)
    else:
        print(1)
        print(c)