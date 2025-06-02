import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):

    n = int(input())

    cloths = {}

    for j in range(n):
        a, b = input().split()

        if b in cloths:
            cloths[b] += 1
        else:
            cloths[b] = 1

    result = 1
    for cloth in cloths:
        result *= cloths[cloth] + 1

    print(result - 1)
