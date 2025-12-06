import sys

input = sys.stdin.readline

N = int(input())

result = N

x = N
i = 2
while i * i <= x:
    if x % i == 0:
        while x % i == 0:
            x //= i
        result -= result//i
    i += 1

if x > 1:
    result -= result//x

print(result)