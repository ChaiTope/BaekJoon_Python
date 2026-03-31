import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    count = 0
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    for j in range(n):
        cx, cy, r = map(int, input().split())

        # 시작점이 원 안에 있는지
        start_in = (x1 - cx) ** 2 + (y1 - cy) ** 2 < r ** 2

        # 도착점이 원 안에 있는지
        end_in = (x2 - cx) ** 2 + (y2 - cy) ** 2 < r ** 2

        if start_in != end_in:
            count += 1

    print(count)