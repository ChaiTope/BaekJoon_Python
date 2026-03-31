import sys

input = sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))

l = 0
r = 0
cnt = 0
current_sum = A[0]

while l <= r < N:
    if current_sum == M:
        cnt += 1
        r += 1
        if r < N:
            current_sum += A[r]

    elif current_sum < M:
        r += 1
        if r < N:
            current_sum += A[r]

    else:
        current_sum -= A[l]
        l += 1

        if r < l < N:
            r = l
            current_sum = A[l]

print(cnt)