import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
T = deque(list(map(int, input().split())))

stack = []
res = []
idx = 1

while T:
    f = T.popleft()

    while stack and stack[-1][1] < f:
        stack.pop()

    if stack:
        res.append(stack[-1][0])
    else:
        res.append(0)

    stack.append((idx, f))
    idx += 1

print(*res)