import sys

input = sys.stdin.readline
T = int(input())

for i in range(T):
    N = int(input())
    P = sorted([list(map(int, input().split())) for _ in range(N)])

    min_y = P[0][1]
    count = 1

    for px, py in P[1:]:
        if py < min_y:
            min_y = py
            count += 1

    print(count)