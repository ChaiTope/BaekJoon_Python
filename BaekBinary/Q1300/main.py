import sys

input = sys.stdin.readline
N = int(input())
K = int(input())
left = 1
right = K

def cnt(x):
    global N
    count = 0
    for i in range(1, N+1):
        count += min(N, x // i)

    return count

while left <= right:
    mid = (left + right) // 2
    count = cnt(mid)

    if count < K:
        left = mid + 1
    else:
        right = mid - 1

print(left)