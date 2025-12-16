import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [False for _ in range(N + 1)]
    done = [False for _ in range(N + 1)]
    cnt_cycle = 0
    for i in range(1, N + 1):
        cur = i
        path = []
        pos = {}

        while True:
            if done[cur]:
                break

            if cur in pos:
                depth = len(path) - pos[cur]
                cnt_cycle += depth
                break

            pos[cur] = len(path)
            path.append(cur)
            cur = arr[cur]

        while path:
            done[path[-1]] = True
            path.pop()

    print(N - cnt_cycle)