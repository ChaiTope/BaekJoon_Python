import sys

input = sys.stdin.readline

N, K = map(int, input().split())

nums = [int(input()) for _ in range(N)]

left, right = 1, max(nums)
answer = 0

while left <= right:
    mid = (left + right) // 2
    count = sum(x // mid for x in nums)

    if count >= K:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)