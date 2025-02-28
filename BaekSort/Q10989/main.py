import sys

N = int(sys.stdin.readline())
arr = [0] * 10001
for i in range(N):
    n = int(sys.stdin.readline())
    arr[n] += 1

for i in range(10001):
    while arr[i] > 0:
        sys.stdout.write(str(i) + "\n")
        arr[i] -= 1
