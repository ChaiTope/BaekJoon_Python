import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

nums = [i for i in range(1, N + 1)]

queue = deque(nums)

cnt = 1
ans = []
while queue:
    if cnt == M:
        ans.append(queue.popleft())
        cnt = 1
    else:
        queue.append(queue.popleft())
        cnt += 1

print("<" + ", ".join(map(str, ans)) + ">")