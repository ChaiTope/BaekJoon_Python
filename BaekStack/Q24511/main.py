import sys
from collections import deque

# 입력 받기
N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
C = list(map(int, sys.stdin.readline().split()))

queue_values = deque()
for i in range(N):
    if A[i] == 0 :
        queue_values.appendleft(B[i])

for c in C:
    queue_values.append(c)

result = []
for i in range(M):
    result.append(queue_values.popleft())

print(*result)