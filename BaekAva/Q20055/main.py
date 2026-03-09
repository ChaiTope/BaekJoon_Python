import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

dur = deque(map(int, input().split()))

robot = deque([False] * N)

step = 0

zero_cnt = dur.count(0)

while zero_cnt < K:
    step += 1

    dur.rotate(1)
    robot.rotate(1)

    robot[N - 1] = False

    for i in range(N - 2, -1, -1):
        if robot[i] and not robot[i + 1] and dur[i + 1] > 0:
            robot[i] = False
            robot[i + 1] = True
            dur[i + 1] -= 1
            if dur[i + 1] == 0:
                zero_cnt += 1

    if dur[0] > 0 and not robot[0]:
        robot[0] = True
        dur[0] -= 1
        if dur[0] == 0:
            zero_cnt += 1
    robot[N - 1] = False

print(step)