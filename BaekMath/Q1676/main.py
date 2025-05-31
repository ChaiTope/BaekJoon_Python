import sys

input = sys.stdin.readline

N = int(input())

summary = 1
count = 0

for i in range(1, N+1):
    summary *= i
    while summary % 10 == 0:
        summary //= 10
        count += 1

print(count)