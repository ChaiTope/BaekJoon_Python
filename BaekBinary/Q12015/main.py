import sys

input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split()))
tails = []

for num in nums:
    if not tails or num > tails[-1]:
        tails.append(num)
        continue

    l = 0
    r = len(tails)

    while l < r:
        mid = (l + r) // 2
        if tails[mid] < num:
            l = mid + 1
        else:
            r = mid

    tails[l] = num

print(len(tails))