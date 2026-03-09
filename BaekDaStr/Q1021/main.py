import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

targets = list(map(int, input().split()))
queue = deque(n for n in range(1, N+1))
cnt = 0

for target in targets:

    while True:
        idx = queue.index(target)

        if idx == 0:
            queue.popleft()
            break

        """if idx <= len(queue)//2:
            queue.append(queue.popleft())
        else:
            queue.appendleft(queue.pop())"""

        if idx <= len(queue) // 2:
            queue.rotate(-1)
        else:
            queue.rotate(1)

        cnt += 1

print(cnt)