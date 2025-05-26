import sys

input = sys.stdin.readline

N = int(input())

array = set(list(map(int, input().split())))

M = int(input())

nums = list(map(int, input().split()))

for num in nums:
    if num in array:
        print(1)
    else:
        print(0)