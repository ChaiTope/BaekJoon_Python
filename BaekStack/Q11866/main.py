from collections import deque

n, a = map(int, input().split())

arr, final = [],[]

for i in range(n):
    arr.append(i+1)

arr = deque(arr)

while arr:
    arr.rotate(-(a-1))
    final.append(str(arr.popleft()))

print("<" + ", ".join(map(str, final)) + ">")