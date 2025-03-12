from collections import deque

n = int(input())

a = deque(enumerate(list(map(int, input().split())), start=1))
final = []

while a:
    idx, value = a.popleft()
    final.append(idx)

    if value > 0:
        a.rotate(-(value-1))
    else:
        a.rotate(-value)

print(*final)