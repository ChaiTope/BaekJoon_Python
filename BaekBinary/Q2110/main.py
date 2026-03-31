import sys

input = sys.stdin.readline

N, C = map(int, input().split())
array = sorted([int(input()) for _ in range(N)])
left = 1
right = array[-1] - array[0]
ans = 0

while left <= right:
    mid = (left + right) // 2
    count = 1
    last = array[0]
    for co in array:
        if co - last >= mid:
            count += 1
            last = co

    if count >= C:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)