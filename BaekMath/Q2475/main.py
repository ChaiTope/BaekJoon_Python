import sys

input = sys.stdin.readline

array = list(map(int, input().split()))

sum = 0
for i in array:
    sum += i**2
    sum %= 10
print(sum)