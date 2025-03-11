import sys
from collections import deque

n = int(sys.stdin.readline())

que = deque()
for _ in range(n):
    order = sys.stdin.readline().split()
    if order[0] == "push":
        que.append(order[1])

    elif order[0] == "pop":
        print(que.popleft() if que else -1)

    elif order[0] == "size":
        print(len(que))

    elif order[0] == "empty":
        print(0 if que else 1)

    elif order[0] == "front":
        print(que[0] if que else -1)

    elif order[0] == "back":
        print(que[-1] if que else -1)
