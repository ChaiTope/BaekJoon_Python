import sys
from collections import deque

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
C = list(map(int, sys.stdin.readline().split()))

que_count = 0
queue_values = deque()
for i in range(N):
    if A[i] == 0:
        queue_values.append(B[i])
        que_count += 1


result = []

if que_count > 0:
    C = reversed(C)

for c in C:
    if queue_values:
        result.append(queue_values.pop())
    else:
        result.append(c)

print(*result)

#일단 여기까지 하고 더 해보자 뭔가 이상함