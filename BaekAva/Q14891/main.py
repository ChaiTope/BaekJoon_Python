import sys
from collections import deque

input = sys.stdin.readline

cogs = [deque(map(int, input().strip())) for _ in range(4)]
K = int(input())
res = 0

def swing(queue, dist):
    if dist == 1:
        queue.appendleft(queue.pop())
    else:
        queue.append(queue.popleft())

for i in range(K):
    n, d = map(int, input().split())
    dirs = [0, 0, 0, 0]
    dirs[n - 1] = d
    n -= 1

    for j in range(n, 0, -1):
        if cogs[j][6] != cogs[j - 1][2]:
            dirs[j - 1] = -dirs[j]
        else:
            break

    for j in range(n, 3):
        if cogs[j][2] != cogs[j + 1][6]:
            dirs[j + 1] = -dirs[j]
        else:
            break

    for j in range(4):
        if dirs[j] != 0:
            swing(cogs[j], dirs[j])

for i in range(4):
    res += cogs[i][0] * (2 ** i)

print(res)