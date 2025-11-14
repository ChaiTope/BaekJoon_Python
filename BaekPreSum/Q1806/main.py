import sys

input = sys.stdin.readline

N, S = map(int, input().split())

nums = list(map(int, input().split()))

min_val = float('inf')

right, left, ans = 0, 0, nums[0]

while True:
    if ans >= S:
        # 답 후보 갱신
        min_val = min(min_val, right - left + 1)
        # 왼쪽을 줄여본다
        ans -= nums[left]
        left += 1
    else:
        # 더 이상 오른쪽으로 못 늘리면 종료
        if right == N - 1:
            break
        right += 1
        ans += nums[right]

print(0 if min_val == float('inf') else min_val)